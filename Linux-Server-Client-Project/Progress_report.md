## REPORT

### General considerations

This exercise requires a server and a client machine. Both systems were downloaded as virtual machines in virtualbox and set up with the Host-only network adapters. This would ensure no internet interferance with DHCP and DNS services. This is a test environment. 

UBUNTU SERVER 22.04

![image](https://github.com/gustavoalito/BeCode/assets/133368766/f8d11ec4-6d39-4323-b6e1-5e3819138a9d)

Linux Mint client XFCE

![image](https://github.com/gustavoalito/BeCode/assets/133368766/b39b89f6-36ef-45a2-9774-d5dc3fa29099)

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

If I ever need to set the root's word, then I can follow this link: https://www.server-world.info/en/note?os=Ubuntu_22.04&p=initial_conf&f=2

---

# 3 -

Install "fail2ban": https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-22-04

Then, configure email: https://technicalramblings.com/blog/how-to-add-email-notifications-to-fail2ban/#adding-the-action => This part didn't work.

---

# 4 -

Followed the video: https://www.youtube.com/watch?v=1csFmQeXHlg&t=462s

The server's IP address is 192.168.24.1/24 (enp0s8).
That means:

|   |   |
|---|---|
|IP Address:|192.168.24.1|
|Network Address:|192.168.24.0|
|Usable Host IP Range:|192.168.24.1 - 192.168.24.254|
|Broadcast Address:|192.168.24.255|
|Total Number of Hosts:|256|
|Number of Usable Hosts:|254|
|Subnet Mask:|255.255.255.0|

- Install isc-dhcp-server
- edit the configuration file (sudo nano /etc/default/isc-dhcp-server)
	- Edit the line where interfacev4 is: INTERFACEV4="enp0s8". Save it.
- Now, we're going to setup the IP pool in /etc/dhcp/dhcpd.conf
	- Uncomment all the commands below the section that starts with "A slightly different..."
	- Add the correct subnet: 192.168.24.0, subnet mask 255.255.255.0
	- Range of IP addresses: 192.168.24.100 192.168.24.200
	- DNS server 192.168.24.1
	- Domain name "mylocaldomain.local"
	- Gateway 192.168.24.1
	- Broadcast address 192.168.24.255
	- Save and close it.
- Restart the dhcp service: sudo systemctl restart isc-dhcp-server
- Check its status: sudo systemctl status isc-dhcp-server
- Allow inbound connections from clients requesting an IP address
	- sudo netstat -anp | grep dhcp (this will show the port the dhcp is listening on). In this case, it's port 67 and UDP protocol.
	-  sudo ufw allow 67/udp
	- Check if firewall rule was correctly added: sudo ufw status.


**Testing a connection to the DHCP server**

Pinging the server and client works and the client machine has a correctly assigned IP address.

*Firewall*

Follow the steps in the server_hardening documentation, and the DHCP video also helps in allowing the DHCP connection. For further information (and it will be useful later when other services are added), I'll follow this tutorial: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04

## DNS
Followed this tutorial: https://www.cherryservers.com/blog/how-to-install-and-configure-a-private-bind-dns-server-on-ubuntu-22-04

- LAN subnet is 192.168.24.0/24
- DNS server's (bindserver's) IP address is 192.168.24.1
- Client's IP address is 192.168.24.101
- Domain is mylocaldomain.local

Install 3 packages: bind9, bind9utils and bind9-doc

Configuration file to be edited: /etc/bind/named.conf.options

![Pasted image 20230614101159](https://github.com/gustavoalito/BeCode/assets/133368766/551e5789-19a8-4a5f-8fdd-f0bcc1bdfe23)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/4a138e5e-562c-4dd3-883c-635686de7245)


After you make the changes, check the syntax of the file with the `named-checkconf` command:

```bash
named-checkconf /etc/bind/named.conf.options
```

If you want to see more verbose output on a successful test, add the `-p` switch to the command (`named-checkconf -p`).

*Edit the named.conf.local file*

![image](https://github.com/gustavoalito/BeCode/assets/133368766/6a9b0573-1de5-4d11-83ef-f84a049a8335)


create a directory to store the zone files we specified in the previous step.

```bash
mkdir /etc/bind/zones
```

*Create the forward zone file*

Now, we'll create a corresponding zone file `/etc/bind/zones/db.fwd.mylocaldomain.local`. The forward zone file allows the Bind DNS server to resolve names (like `ns.mylocaldomain.local`) to IP addresses (like `192.168.24.1`).

First, copy the default db.local zone file to `/etc/bind/zones/db.fwd.mylocaldomain.local`:

```bash
cp /etc/bind/db.local /etc/bind/zones/db.fwd.mylocaldomain.local
```
![image](https://github.com/gustavoalito/BeCode/assets/133368766/9f6f981a-57a3-4183-8413-ef5f08ea3977)

Now, creating the reverse zone file is quite similar.

First, copy the default db.local zone file to `/etc/bind/zones/db.rev.mylocaldomain.local`

```bash
cp /etc/bind/db.127 /etc/bind/zones/db.rev.mylocaldomain.local
```
![image](https://github.com/gustavoalito/BeCode/assets/133368766/ff613bbe-b86d-436b-9b3e-44fe93007622)

- Restart bind9 (systemctl restart bind9)

## Configure clients to use the configuration

Once the Private Bind DNS server is configured, we can configure the clients to use it. Follow these steps for both `client1` and `client2`.

First, check which interface is used for LAN connectivity with this command:

```bash
ip -brief addr show to 192.168.24.0/24

```

The interface we need will be the first value displayed. For example, `enp0s8` in the output below:

```bash
enp0s8             UP             192.168.24.1/24
```

Next, edit your `netplan` YAML file to include a DNS configuration that points to the private Bind DNS server. Typically, `netplan` configuration files are stored at `/etc/netplan`.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/0f58a027-59b0-4f8d-86f5-3c2f038e98e1)

Once you the configuration is complete, test it with this command:

```bash
netplan try
```

Press `ENTER` to accept the changes.

Now, configure the `nameserver` for the file `etc/resolv.conf`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/2b3656b5-f25d-4f43-979c-5e8b2769d79c)


## Testing the configuration

Using these commands, check whether they resolve into an address on a client machine:

- `nslookup ns.mylocaldomain.local`
- `nslookup mylocaldomain.local`



Mixed success. They are all going through the DNS server (192.168.24.1) but don't get resolved.

# Don't forget to allow bind9 or port 53 (default DNS server's port) in the server's firewall!!

---

## HTTP, mariadb (internal website running GLPI)

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

Test it via the command: `sudo mysql -u admin -p`

![Pasted image 20230614142431](https://github.com/gustavoalito/BeCode/assets/133368766/3475b059-c893-4f08-b5e4-2d58ee057a9a)


Create a new database for GLPI. In the MariaDB shell, run the following commands:

`CREATE DATABASE glpidb;
`GRANT ALL PRIVILEGES ON glpidb.* TO 'glpiuser'@'localhost' IDENTIFIED BY 'password';
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

- Connecting to the GLPI interface on the client via the browser: `192.168.1.24/glpi

The easiest way is to follow this video: 
https://www.youtube.com/watch?v=X3jbo6rFntI&t=458s

Or, follow this tutorial:
https://unixcop.com/how-to-install-glpi-on-ubuntu-22-04/

Download link:
`cd /tmp/ wget https://github.com/glpi-project/glpi/releases/download/10.0.7/glpi-10.0.7.tgz


![Pasted image 20230615105519](https://github.com/gustavoalito/BeCode/assets/133368766/ca897fef-1c3c-47f9-8a07-a5e004485981)


Change the passwords of the accounts above.

---

## Backup + cron job

First things first. Check the server's timezone to be sure it is the correct one.

use the command `timedatectl
`timedatectl set-timezone Europe/Brussels`

Further info: https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-check-and-set-timezone-in-ubuntu-20-04/

For the backup, I'll try to mount the partition I created for the backup, create the backup and then unmount it.

The command `lsblk`  which lists information about all available block devices, including disks and partitions.

![Pasted image 20230615122836](https://github.com/gustavoalito/BeCode/assets/133368766/3bbe3944-695d-40b6-96f5-21a59ff9b906)


It is **sda2**.

Script named = backup_conf_files.sh
Located at: /usr/local/bin

- Reference: https://ubuntu.com/server/docs/backups-shell-scripts

Backup script:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/35c483ce-c8cc-4064-8f63-e2c29391031e)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/d42025a4-bf87-4434-9f34-4ca6b2c6c740)


![ff2e-148d-4bcc-aaaf-83752c0712f7](https://github.com/gustavoalito/BeCode/assets/133368766/45fba618-e245-4980-a8f2-e51918ba9685)


Reference for date formatting: https://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/

Created a cron job for everyday at 10h.

Use the command `sudo crontab -e`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/2f83791c-7a04-4bef-84dd-90ff26758a1b)

The script will log its operations in the log file `/var/log/backup.log`, including errors. 

---

## Setting up the client machine (Linux Mint)

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


![Pasted image 20230615152346](https://github.com/gustavoalito/BeCode/assets/133368766/b82575e9-03e6-41da-9e5c-c674bb4634f3)


1. Select the remaining free space and click the "+" button to create a new partition.
2. Configure the partition as follows:
    - Size: Leave the remaining space as it is to be used for the root partition.
    - Type for the new partition: Select "Logical".
    - Location for the new partition: Select "Beginning of this space".
    - Use as: Select "Ext4 journaling file system".
    - Mount point: Select "/".
3. Click "OK" to create the partition.

![Pasted image 20230615152611](https://github.com/gustavoalito/BeCode/assets/133368766/cb5ce2e2-4d5a-4865-9bb7-1bf9b94895b6)

![Pasted image 20230615152638](https://github.com/gustavoalito/BeCode/assets/133368766/416dc517-1631-48b8-a86f-21f9d3cae17c)


Verify the Separate /home Partition

1. Open a terminal (Ctrl+Alt+T).
2. Run the command `lsblk` to list the available block devices.
3. Verify that you see two separate partitions, one mounted as "/" and the other mounted as "/home".

![Pasted image 20230615160311](https://github.com/gustavoalito/BeCode/assets/133368766/942a69d0-a446-41b0-90d4-32ef0c1a19fd)


Install LibreOffice, Gimp & Mullvad browser. For Mullvad, you can follow this link: https://www.youtube.com/watch?v=vrgFzihf2rY&t=605s 
