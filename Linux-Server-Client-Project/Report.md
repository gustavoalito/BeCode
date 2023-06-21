## REPORT

### General considerations

NAT network

To get started, the NAT network adapter will be initialized with DHCP enabled. Why? Because the Ubuntu server needs to get its IP address from somewhere. Until we set up a static IP address for it, it will be kept enabled. Down in the process, I'll describe how to set the static IP address so we can disable the NAT network adapter's DHCP option.

# 1 -

The first step was to download the Ubuntu server's ISO file from the official Ubuntu page.
Then, when initially installing it via VirtualBox, I used the following pages to help with the steps:

For the Ubuntu server initial install: https://www.youtube.com/watch?v=YtH9D2SqBqA

For the partition, I chose to make it manually. From the free space available, I created a partition of 2GB and mounted it into "mnt/backup".

=> For the firewall and SSH parts, I'm basing myself on the following [link](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Server_hardenning.md)

---

# 2 -

Following the link for hardening the server, I installed any packs that were necessary to run the commands I'm used to: 
- plocate (for the "locate" command), 
- net-tools (for the "ifconfig" command).

The changes in the ssh_config file were the same as the ones from the documentation. 

*SSH-ing from the client to the server* 

Since the root user in the Ubuntu server is by default disabled, I decided to leave it like this for security reasons. Therefore, I'll test an SSH connection from my client to the server using my "boss" user.

The connection is successful.

If I ever need to set the root's word, then I can follow this link: https://www.server-world.info/en/note?os=Ubuntu_22.04&p=initial_conf&f=2

---

# 3 -

Followed the video: https://www.youtube.com/watch?v=1csFmQeXHlg&t=462s

Do the `ip a` command to gather the IP address and interface name

enp0s3 interface
DHCP server's IP 10.0.2.5/25

IP Address:	10.0.2.0
Network Address:	10.0.2.0
Usable Host IP Range:	10.0.2.1 - 10.0.2.254
Broadcast Address:	10.0.2.255
Total Number of Hosts:	256
Number of Usable Hosts:	254
Subnet Mask:	255.255.255.0

The server's IP address is 10.0.2.5/24 and interface enp0s3.
That means:

|   |   |
|---|---|
|IP Address:|10.0.2.5|
|Network Address:|10.0.2.0|
|Usable Host IP Range:|10.0.2.100 - 10.0.2.254|
|Broadcast Address:|10.0.2.255|
|Total Number of Hosts:|256|
|Number of Usable Hosts:|254|
|Subnet Mask:|255.255.255.0|

- Install isc-dhcp-server
- edit the configuration file (sudo nano /etc/default/isc-dhcp-server)
	- Edit the line where interfacev4 is: INTERFACEV4="enp0s3". Save it.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/95f85305-ce45-4e44-b539-b0b80ff47713)

- Now, we're going to set up the IP pool in /etc/dhcp/dhcpd.conf
	- Uncomment all the commands below the section that starts with "A slightly different..."
	
![image](https://github.com/gustavoalito/BeCode/assets/133368766/df857d40-737b-4124-bd20-ad9e0ea57e7e)

- Restart the dhcp service: sudo systemctl restart isc-dhcp-server
- Check its status: sudo systemctl status isc-DHCP-server
- Allow inbound connections from clients requesting an IP address
	- sudo netstat -anp | grep dhcp (this will show the port the dhcp is listening on). In this case, it's port 67 and UDP protocol.
![image](https://github.com/gustavoalito/BeCode/assets/133368766/39af10ae-1add-46b3-8ef1-27b0670796f9)
	-  sudo ufw allow 67/udp
	- Check if the firewall rule was correctly added: `sudo ufw status verbose`.

## Setting up a static IP address for the Ubuntu server

Create or edit the network configuration file under the `/etc/netplan` directory. Create a configuration file and edit it in an editor:
`sudo nano /etc/netplan/01-netcfg.yaml` 
Add the network configuration in YAML format as below:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/a66c2bf2-ba08-4055-823a-8bb86e97bb80)

Apply the changes by running the following commands:
`sudo netplan apply` 
That’s it. The static IP address is configured on the Ubuntu system.

Now you can disable the NAT network adapter's DHCP option. And of course, restart the Ubuntu server.

**Testing a connection to the DHCP server**

1st and foremost, the client machine, in this case, Linux Mint xfce, needs to have the DHCP's address configured as its `nameserver`.

To do that, we'll need to configure `/etc/resolv.conf` and edit the nameserver to the DHCP's IP address:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/59335e06-d8df-46ad-ac11-6662fc55a8a9)

Pinging the server and client works and the client machine has a correctly assigned IP address.

However, this is not enough, as the client machine relies on the DHCP server for the DNS part as well. We'll configure the DNS server shortly. Meanwhile, we can update and upgrade the client machine by temporarily setting its network adapter to Bridged or NAT to have correct access to the internet and update/upgrade all the packages. 

=> To check the IP addresses leasing from the DHCP server, use the command `dhcp-lease-list`

*Firewall*

Follow the steps in the server_hardening documentation, and the DHCP video also helps in allowing the DHCP connection. For further information (and it will be useful later when other services are added), I'll follow this tutorial: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04

## DNS
Followed this tutorial: https://www.cherryservers.com/blog/how-to-install-and-configure-a-private-bind-dns-server-on-ubuntu-22-04

- LAN subnet is 10.0.2.0/24
- DNS server's IP address is 10.0.2.5
- Client's IP address is 10.0.2.101
- Domain is example.org

Install 3 packages: bind9, bind9utils and bind9-doc

Configuration file to be edited: /etc/bind/named.conf.options

![image](https://github.com/gustavoalito/BeCode/assets/133368766/2b92acb8-1fa4-4044-8869-bb9152a843fc)


These forwarders will be used if the DNS server needs to resolve domain names outside the configured zone. The address used is Google's DNS.

Save the changes and exit the text editor.

Restart the DNS service: `sudo systemctl restart bind9`

To test your query time we can use the dig command which is installed by the dnsutils package.

`dig google.com`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/4e783c03-a414-4a1a-8bc3-7c5077dfd4ed)

### Configure the DNS zone

For a primary master server configuration, the DNS gets the data for a zone from a file stored on its host. Also, the DNS has control of that zone. Now let’s say we have a domain called “example.org”. We are going to configure the DNS to be the primary master for that domain.

### Forward Zone File

Step 1. Open and edit the /etc/bind/named.conf file.

`sudo nano /etc/bind/named.conf`

Ensure that it contains the following lines and they are *NOT* commented out:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/68e3c81e-664c-4db9-aea5-47b7a5befab7)

Step 2. Open and edit the /etc/bind/named.conf.local file to add a DNS zone.

`sudo nano /etc/bind/named.conf.local`

Add the following block to it:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/b7737f6c-c0f2-4ed2-8f94-d8bfd135946c)

Step 3. Create a zone file from the template one.

sudo cp /etc/bind/db.local /etc/bind/db.example.org
Step 4. Now open the new example zone file.

`sudo nano /etc/bind/db.example.com`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/79753efa-bed3-4a96-8702-c82222a57cf4)

Please note that you have to increase the Serial Number every time you make changes to the zone files.

In the above configuration:

- **$TTL** defines the default Time-to-Live value for the records in the zone file.
- **SOA** specifies the Start of Authority record, including the primary nameserver and the contact email address.
- **NS** defines the nameserver record for the zone.
- **A** records map hostnames to IP addresses. In this case, server.example.org is assigned the IP address 10.0.2.5, and client1 is assigned the IP address 10.0.2.101.

Step 5. Restart DNS Service to apply changes.

`sudo systemctl restart bind9`

### Reverse Zone File

Now to map an IP to a name you have to configure the reverse zone file.

Step 1. Edit the /etc/bind/named.conf.local file.

`sudo nano /etc/bind/named.conf.local`

Make the changes below: 

![image](https://github.com/gustavoalito/BeCode/assets/133368766/676555b7-dc47-4b49-bcc5-fb0d318be8e8)

10.0.2 is the first three octets of the network.

Step 2. Create the  `/etc/bind/db.10` file from template one.

`sudo cp /etc/bind/db.127 /etc/bind/db.10`

Step 3. Edit the /etc/bind/db.10 file.

`sudo nano /etc/bind/db.10`

Make the changes below:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/119dd4d5-695c-4a96-afdf-83627f4909ca)

Step 4. Restart DNS Service to apply changes.

### Configuration Files Verification

Step 1. Execute the following commands to check if it will return any errors.

`named-checkzone example.org /etc/bind/db.example.com
named-checkzone 10.0.2.0/24 /etc/bind/db.10
named-checkconf /etc/bind/named.conf.local
named-checkconf /etc/bind/named.conf`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/5878c3a7-bafa-4fd8-a2ed-daceb265c76b)

## Testing the configuration

The client needs to be configured to look up the DNS and the domain server name. For that, we need to edit the /etc/resolv.conf file.

**resolv.conf**

The first step in testing BIND9 is to add the nameserver’s IP Address to a host's resolver. The Primary nameserver should be configured as well as another host to double-check things. Refer to DNS client configuration for details on adding nameserver addresses to your network clients. In the end, your nameserver line in /etc/resolv.conf should be pointing at 10.0.2.5 and you should have a search parameter for your domain. Something like this:

`nameserver  10.0.2.5
search example.org`

Once this is done, restart the networking service:

`sudo systemctl restart networking`
Using these commands, check whether they resolve into an address on a client machine:

- `nslookup example.org`
- `dig example.org`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/b1074982-c266-4afb-a3c7-58b5017fc292)

They are all going through the DNS server (10.0.2.5) and are being resolved - internally and externally.

**Don't forget to allow bind9 or port 53 (default DNS server's port) in the server's firewall!!**

---

## HTTP, mariadb (internal website running GLPI)

Install apache2 (HTTP) server:

`sudo apt install apache2`

Since we're on an install frenzy, let's install a few other packages that will be required for GLPI (further down the line).

`sudo apt install -y php-curl php-xml php-zip php-gd php-intl php-intl php-pear php-imagick php-imap php-memcache php-pspell php-tidy php-xmlrpc php-xsl php-mbstring php-ldap php-cas php-apcu libapache2-mod-php php-mysql php-bz2`

Reload apache2:

`sudo systemctl reload apache2`

## Install MariaDB (MySQL) server

`sudo apt install mariadb-server`

Once MariaDB is installed, you can secure the installation by running the following command:

`sudo mysql_secure_installation`

Follow the instructions in the terminal and select the options that make more sense in terms of security: no root login, remove test user and database.
	
Create a new account called **admin** with the same capabilities as the **root** account, but configured for password authentication. Open up the MariaDB prompt from your terminal:

`sudo mariadb`

`GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

Test it via the command: `sudo mysql -u admin -p`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/d9d9ea45-528b-483e-8891-01eeb2533d38)

Create a new database for GLPI. In the MariaDB shell, run the following commands:

`CREATE DATABASE glpidb;
`GRANT ALL PRIVILEGES ON glpidb.* TO 'glpi'@'localhost' IDENTIFIED BY 'password';
`FLUSH PRIVILEGES;
`EXIT;

### Install PHP and necessary modules:

`sudo apt install php libapache2-mod-php php-mysql -y

Restart Apache for the changes to take effect:

`sudo systemctl restart apache2`

### Firewall

sudo ufw allow 80 
sudo ufw allow 443

Port 80 enables HTTP. Port 443, HTTPS (encrypted).

Up to this point, we should have the firewall configured with the following rules:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/7ce9b0f4-05bd-49ab-9705-e044762cd1ef)


### Installing GLPI

Installing GLPI on Ubunutu:

The easiest way is to follow this video: 
https://www.youtube.com/watch?v=X3jbo6rFntI&t=458s


Download link:
`cd /tmp/ wget https://github.com/glpi-project/glpi/releases/download/10.0.7/glpi-10.0.7.tgz`

Now unzip the archive:

`tar -xvf glpi-10.0.2.tgz`

Move it to the Apache root directory:

`sudo mv glpi /var/www/html/`

Assign appropriate permissions:

`sudo chmod 755 -R /var/www/html/`

And make Apache the owner of it:

`sudo chown www-data:www-data -R /var/www/html/`

Now we can continue the installation through the client's browser. Note the Ubuntu server's IP address (ip a command): 10.0.2.5

Go to the client machine, open a browser, and open `10.0.2.5/glpi`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/7d8579b7-7ade-4c7f-88ed-ba89fe8a787e)

Follow the instructions on the screen.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/2f2ff905-4b1f-4aa4-8b4c-e6c698d49492)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/251750b4-8d1e-47b7-9e6d-8d38011bca3c)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/78b9f632-8b84-4722-9272-b3e4a6a28310)
Change the passwords of the accounts above.

Test connection using the default glpi user and password from the screenshot above.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/f3687d9c-49fa-46e5-86f7-feb87418eabd)

---

## Backup + cron job

First things first. Check the server's timezone to be sure it is the correct one.

use the command timedatectl:
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

*NOTE: If a backup is ever needed to be restored, use the command `tar xvpfz backup.tgz -C /` inside the backup folder.

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


Install LibreOffice, Gimp & Mullvad browser. For Mullvad, you can follow this link: https://www.youtube.com/watch?v=vrgFzihf2rY&t=605s => or simply search for it in the "Software Manager" and install it from there. It's way easier ;)
