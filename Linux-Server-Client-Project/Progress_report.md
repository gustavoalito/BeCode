## PROGRESS REPORT


# 1 -

First step was to download the Ubuntu server's ISO file from the official Ubuntu page.
The, when initially installing it via VirtualBox, I used the following pages to help with the steps:

For the Ubuntu server initial install: https://www.youtube.com/watch?v=YtH9D2SqBqA

For the partition, I chose to make it manually. From the free space available, I created a partition of 2GB and mounted it into "mnt/backup".

---

# 2 -

Following the link for hardening the server, I installed any packs that were necessary to run the commands I'm used to: 
- plocate (for the "locate" command), 
- net-tools (for the "ifconfig" command) .

The changes in the ssh_config file were the same as the ones from the documentation. 

*SSH-ing from Kali to the server* 

Since the root user in the Ubuntu server is by default disabled, I decided to leave it like this for security reasons. Therefore, I'll test an SSH connection from my Kali to the server using my "boss" user.

The connection is successful.

If I ever need to set the root's password, then I can follow this link: https://www.server-world.info/en/note?os=Ubuntu_22.04&p=initial_conf&f=2

---

# 3 -

Install "fail2ban": https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-22-04

Then, configure email: https://technicalramblings.com/blog/how-to-add-email-notifications-to-fail2ban/#adding-the-action => This part didn't work.

---

# 4 -

Followed the video: https://www.youtube.com/watch?v=1csFmQeXHlg&t=462s

The server's IP address is 10.40.6.74/16 (enp0s3).
That means:

|   |   |
|---|---|
|IP Address:|10.40.6.74|
|Network Address:|10.40.0.0|
|Usable Host IP Range:|10.40.0.2 - 10.40.0.20|
|Broadcast Address:|10.40.255.255|
|Total Number of Hosts:|65.536|
|Number of Usable Hosts:|65.534|
|Subnet Mask:|255.255.0.0|

- Install isc-dhcp-server
- edit the configuration file (sudo nano /etc/default/isc-dhcp-server)
	- Edit the line where interfacev4 is: INTERFACEV4="enp0s3". Save it.
- Now, we're going to setup the IP pool in /etc/dhcp/dhcpd.conf
	- Uncomment all the commands below the section that starts with "A slightly different..."
	- Add the correct subnet: 10.40.0.0, subnet mask 255.255.0.0
	- Range of IP addresses: 10.40.0.2 10.40.0.20
	- DNS server server.example.org
	- Domain name example.org
	- Gateway 10.40.0.1
	- Broadcast address 10.40.255.255
	- Save and close it.
- Restart the dhcp service: sudo systemctl restart isc-dhcp-server
- Check its status: sudo systemctl status isc-dhcp-server
- Allow inbound connections from clients requesting an IP address
	- sudo netstat -a,np | grep dhcp (this will show the port the dhcp is listening on). In this case, it's port 67 and UDP protocol.
	-  sudo ufw allow 67/udp
	- Check if firewall rule was correctly added: sudo ufw status.


**Testing a connection to the DHCP server**

The DHCP server is up and running, however, the only way I managed to make the client (temporarily, it is Kali) to obtain an IP address from the server's pool was by turning off the internet and restarting Kali.

Pinging the server and client works and turning back on the internet, Kali has a correctly assigned IP address.

*Firewall*

Follow the steps in the server_hardening documentation, and the DHCP video also helps in allowing the DHCP connection. For further information (and it will be useful later when other services are added), I'll follow this tutorial: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04

**DNS
Followed this tutorial: https://www.cherryservers.com/blog/how-to-install-and-configure-a-private-bind-dns-server-on-ubuntu-22-04

- LAN subnet is 10.40.0.0/16
- DNS server's (bindserver's) IP address is 10.40.6.74
- Client's IP address is 10.40.0.7
- Domain is example.org

Install 3 packages: bind9, bind9utils and bind9-doc

Configuration file to be edited: /etc/bind/named.conf.options

![[Pasted image 20230614101159.png]]

After you make the changes, check the syntax of the file with the `named-checkconf` command:

```bash
named-checkconf /etc/bind/named.conf.options
```

If you want to see more verbose output on a successful test, add the `-p` switch to the command (`named-checkconf -p`).

*Edit the named.conf.local file*

![[Pasted image 20230614115956.png]]

create a directory to store the zone files we specified in the previous step.

```bash
mkdir /etc/bind/zones
```

*Create the forward zone file*

Now, we'll create a corresponding zone file `/etc/bind/zones/example.org`. The forward zone file allows the Bind DNS server to resolve names (like `bindserver.example.org`) to IP addresses (like `10.40.6.74`).

First, copy the default db.local zone file to `/etc/bind/zones/example.org`:

```bash
cp /etc/bind/db.local /etc/bind/zones/example.org
```

![[Pasted image 20230614120316.png]]

Now, creating the reverse zone file is quite similar.

First, copy the default db.local zone file to `/etc/bind/zones/example.org.rev`

```bash
cp /etc/bind/db.127 /etc/bind/zones/example.org.rev
```

![[Pasted image 20230614120522.png]]

- Restart bind9 (systemctl restart bind9)

*Configure clients to use the configuration

Once the Private Bind DNS server is configured, we can configure the clients to use it. Follow these steps for both `client1` and `client2`.

First, check which interface is used for LAN connectivity with this command:

```bash
ip -brief addr show to 10.40.0.0/16

```

The interface we need will be the first value displayed. For example, `eth1` in the output below:

```bash
eth0             UP             10.40.0.5/16
```

Next, edit your `netplan` YAML file to include a DNS configuration that points to the private Bind DNS server. Typically, `netplan` configuration files are stored at `/etc/netplan`.

![[Pasted image 20230614120946.png]]

Once you the configuration is complete, test it with this command:

```bash
netplan try
```

Press `ENTER` to accept the changes.

## Testing the configuration

Using these commands, check whether they resolve into an address on a client machine:

- `nslookup client1`
- `nslookup client2`
- `nslookup bindserver`
- `nslookup client1.example.org`
- `nslookup client2.example.org`
- `nslookup bindserver.example.org`

![[Pasted image 20230614121300.png]]
Success! They are all going through the DNS server (10.40.6.74).

# Don't forget to allow bind9 or port 53 (default DNS server's port) in the server's firewall!!

---


Install apache2

Apache (HTTP) server:

`sudo apt install apache2


Install MariaDB (MySQL) server:

`sudo apt install mariadb-server`

Once MariaDB is installed, you can secure the installation by running the following command:

`sudo mysql_secure_installation`

Create a new account called **admin** with the same capabilities as the **root** account, but configured for password authentication. Open up the MariaDB prompt from your terminal:

`sudo mariadb`

`GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

usr: admin
pass: mariaboss

Test it via the command: `sudo mysql -u admin -p`

![[Pasted image 20230614142431.png]]

Create a new database for GLPI. In the MariaDB shell, run the following commands:

`CREATE DATABASE glpidb;
`GRANT ALL PRIVILEGES ON glpidb.* TO 'glpiuser'@'localhost' IDENTIFIED BY 'glpiboss';
`FLUSH PRIVILEGES;
`EXIT;

Install PHP and necessary modules:

`sudo apt install php libapache2-mod-php php-mysql -y

Restart Apache for the changes to take effect:

`sudo systemctl restart apache2`

### Firewall

sudo ufw allow 80 
sudo ufw allow 443

### Installing GLPI

Installing GLPI on Ubunutu:

The easiest way is to follow this video: 
https://www.youtube.com/watch?v=X3jbo6rFntI&t=458s

Or, follow this tutorial:
https://unixcop.com/how-to-install-glpi-on-ubuntu-22-04/

Download link:
`cd /tmp/ wget https://github.com/glpi-project/glpi/releases/download/10.0.7/glpi-10.0.7.tgz


![[Pasted image 20230615105519.png]]

Change the passwords of the accounts above.

---

First things first. Check the server's timezone to be sure it is the correct one.

use the command `timedatectl
`timedatectl set-timezone Europe/Brussels`

Further info: https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-check-and-set-timezone-in-ubuntu-20-04/

For the backup, I'll try to mount the partition I created for the backup, create the backup and then unmount it.

The command `lsblk`  which lists information about all available block devices, including disks and partitions.

![[Pasted image 20230615122836.png]]

It is **sda2**.

Script named = backup_conf_files.sh
Located at: /usr/local/bin

- Reference: https://ubuntu.com/server/docs/backups-shell-scripts

Backup script:

![[Pasted image 20230615144034.png]]
![[Pasted image 20230615144100.png]]


Reference for date formatting: https://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/

Created a cron job for every Mon, Wed and Fri at 09:13.

Use the command `sudo crontab -e`


![[Pasted image 20230615145219.png]]

---


Downloaded Linux Mint xfce version (light version).

**REQUIREMENT**  => The /home folder is located on a separate partition, same disk. For this I'll use this reference:
https://linuxmint-installation-guide.readthedocs.io/en/latest/partitioning.html


1. During the Linux Mint XFCE installation, choose the "Something else" option for partitioning when prompted.
2. You will see a list of available disks. Select the disk you created in VirtualBox (e.g., /dev/sda) and click "New Partition Table" to create a new partition table.
3. Once the new partition table is created, click on the "Free Space" entry and click the "+" button to create a new partition.
4. Configure the partition as follows:
    - Size: Enter the desired size for the /home partition (e.g., 10GB).
    - Type for the new partition: Select "Logical".
    - Location for the new partition: Select "Beginning of this space".
    - Use as: Select "Ext4 journaling file system".
    - Mount point: Select "/home".
5. Click "OK" to create the partition.


![[Pasted image 20230615152346.png]]

1. Select the remaining free space and click the "+" button to create a new partition.
2. Configure the partition as follows:
    - Size: Leave the remaining space as it is to be used for the root partition.
    - Type for the new partition: Select "Logical".
    - Location for the new partition: Select "Beginning of this space".
    - Use as: Select "Ext4 journaling file system".
    - Mount point: Select "/".
3. Click "OK" to create the partition.

![[Pasted image 20230615152611.png]]

![[Pasted image 20230615152638.png]]

Verify the Separate /home Partition

1. Open a terminal (Ctrl+Alt+T).
2. Run the command `lsblk` to list the available block devices.
3. Verify that you see two separate partitions, one mounted as "/" and the other mounted as "/home".

![[Pasted image 20230615160311.png]]

Install LibreOffice & Gimp. 