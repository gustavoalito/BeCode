## REPORT

### Index
- [Index](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)
- [General condiderations](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#general-considerations)
- [Setting up the Ubuntu server](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#setting-up-the-ubuntu-server)
- [Server hardening](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#server-hardening)
- [Setting up DHCP](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#setting-up-dhcp)
- [Setting up a static IP address for the Ubuntu server](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#setting-up-a-static-ip-address-for-the-ubuntu-server)
- [DNS](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#dns)
- [Configure the DNS zone](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#configure-the-dns-zone)
- [Forward Zone File](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#forward-zone-file)
- [Reverse Zone File](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#reverse-zone-file)
- [Configuration Files Verification](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#configuration-files-verification)
- [Testing the DNS configuration in the client](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#testing-the-dns-configuration-in-the-client)
- [HTTP, mariadb (internal website running GLPI)](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#http-mariadb-internal-website-running-glpi)
- [Install MariaDB (MySQL) server](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#install-mariadb-mysql-server)
- [Install PHP and necessary modules](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#install-php-and-necessary-modules)
- [Firewall](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#firewall)
- [Installing GLPI](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#installing-glpi)
- [Backup + cron job](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#backup--cron-job)
- [Setting up the client machine (Linux Mint)](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#setting-up-the-client-machine-linux-mint)
- [Troubleshooting](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#troubleshooting)
- [Lessons-learned](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#lessons-learned)

---

### General considerations

**NAT network**

Creating a NAT network is an easier way to manage the VMs subnet in VirtualBox. You can set it up as shown in the screenshot(s) below. I'm using the network IP 10.0.2.0/24. That means that all VMs using this NAT network adapter will fall into this subnet and will also have internet access.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/b67c67f2-c919-4cbe-856d-2cbfd8e7fe0a)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/c1334d2b-a6ac-48ce-8449-190f545feddc)

Please note the option "Enable DHCP". Later in the process, this option will be disabled. But to get started, since there's no other VM under this subnet, then the 1st VM needs to get its IP address somehow.

Hence, the NAT network adapter will be initialized with DHCP enabled to get started. Why? Because the Ubuntu server needs to get its IP address from somewhere. Until we set up a static IP address for it, it will be kept enabled. In the process, I'll describe how to set the static IP address so we can disable the NAT network adapter's DHCP option.

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

# Setting up the Ubuntu server

The first step was to download the Ubuntu server's ISO file from the official Ubuntu page.
Then, when initially installing it via VirtualBox, I used the following pages to help with the steps:

For the Ubuntu server initial install: https://www.youtube.com/watch?v=YtH9D2SqBqA

For the partition, I chose to make it manually. From the free space available, I created a partition of 2GB and mounted it into "mnt/backup".

=> For the firewall and SSH parts, I'm basing myself on the following [link](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Server_hardenning.md)

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

# Server hardening

Following the link for hardening the server, I installed any packs that were necessary to run the commands I'm used to: 
- plocate (for the "locate" command), 
- net-tools (for the "ifconfig" command).

The changes in the ssh_config file were the same as the ones from the documentation. 

*SSH-ing from the client to the server* 

Since the root user in the Ubuntu server is by default disabled, I decided to leave it like this for security reasons. Therefore, I'll test an SSH connection from my client to the server using my "boss" user.

The connection is successful.

If I ever need to set the root's word, then I can follow this link: https://www.server-world.info/en/note?os=Ubuntu_22.04&p=initial_conf&f=2

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

# Setting up DHCP

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

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

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
![image](https://github.com/gustavoalito/BeCode/assets/133368766/11e13107-0f65-4887-9f1f-7092015f2079)

*Firewall*

Follow the steps in the server_hardening documentation, and the DHCP video also helps in allowing the DHCP connection. For further information (and it will be useful later when other services are added), I'll follow this tutorial: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-22-04

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

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

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

### Configure the DNS zone

For a primary master server configuration, the DNS gets the data for a zone from a file stored on its host. Also, the DNS has control of that zone. Now let’s say we have a domain called “example.org”. We are going to configure the DNS to be the primary master for that domain.

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

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

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

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

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

### Configuration Files Verification

Step 1. Execute the following commands to check if it will return any errors.

`named-checkzone example.org /etc/bind/db.example.com
named-checkzone 10.0.2.0/24 /etc/bind/db.10
named-checkconf /etc/bind/named.conf.local
named-checkconf /etc/bind/named.conf`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/5878c3a7-bafa-4fd8-a2ed-daceb265c76b)

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

### Testing the DNS configuration in the client

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

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

## HTTP, mariadb (internal website running GLPI)

Install apache2 (HTTP) server:

`sudo apt install apache2`

Since we're on an install frenzy, let's install a few other packages that will be required for GLPI (further down the line).

`sudo apt install -y php-curl php-xml php-zip php-gd php-intl php-intl php-pear php-imagick php-imap php-memcache php-pspell php-tidy php-xmlrpc php-xsl php-mbstring php-ldap php-cas php-apcu libapache2-mod-php php-mysql php-bz2`

Reload apache2:

`sudo systemctl reload apache2`

### Install MariaDB (MySQL) server

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

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

### Install PHP and necessary modules

`sudo apt install php libapache2-mod-php php-mysql -y

Restart Apache for the changes to take effect:

`sudo systemctl restart apache2`

### Firewall

sudo ufw allow 80 
sudo ufw allow 443

Port 80 enables HTTP. Port 443, HTTPS (encrypted).

Up to this point, we should have the firewall configured with the following rules:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/7ce9b0f4-05bd-49ab-9705-e044762cd1ef)

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

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

One last trick, let's secure (and at the same time) back up the installation php file for security reasons. 

`cd /var/www/html/glpi/install
sudo mv install.php install.php.bak
sudo systemctl restart apache2`

After this trick, one warning message from the GLPI home screen should disappear.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/354dd319-4d49-4d70-b903-1df63158a175)

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

## Backup + cron job

First things first. Check the server's timezone to be sure it is the correct one.

use the command timedatectl:
`timedatectl set-timezone Europe/Brussels`

Further info: https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-check-and-set-timezone-in-ubuntu-20-04/

For the backup, I'll try to mount the partition I created for the backup, create the backup and then unmount it.

The command `lsblk`  which lists information about all available block devices, including disks and partitions.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/9555dbd0-2b96-4e30-87b0-e3120999e6cc)

It is **sda2**.

Script named: **backup_conf_files.sh**
Located at: **/usr/local/bin**

- Reference: https://ubuntu.com/server/docs/backups-shell-scripts

Backup script:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/ec3d2b41-aee7-4dab-a4fb-15c1cc59c279)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/54a1609e-491a-49e6-9b64-3683d6580c9c)

![ff2e-148d-4bcc-aaaf-83752c0712f7](https://github.com/gustavoalito/BeCode/assets/133368766/45fba618-e245-4980-a8f2-e51918ba9685)

Apologies for all the SLEEP commands. I like to see the script executed step by step xD

=> Make sure the script has the correct permissions. In this case, it is owned by root. No problem with that. Just add execution permissions to it: `sudo chmod +x backup_conf_files.sh`

Test it by running it: `sudo ./backup_conf_files.sh`

=> Note that you'll need to manually mount the partition in order to see the backup once it's finished: `mount /dev/sda2 /mnt/backup` and then unmount it `umount /mnt/backup`.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/ee8a96a7-851d-49af-907a-b7477342d18c)


![image](https://github.com/gustavoalito/BeCode/assets/133368766/70a0a4e8-b75b-44e4-a193-b8154394cb7d)

=> I repeat, don't forget to unmount it, making sure you navigate away from the directory (otherwise it will not be able to unmount the partition): `sudo umount /mnt/backup` 

Reference for date formatting: https://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/

Created a cron job to run this backup script once a week.

Use the command `sudo crontab -e`. If you don't have this package, install it `sudo apt install cron`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/7719c819-8f82-4e2f-bb4d-9a52f8f54a4e)

The script will log its operations in the log file `/var/log/backup.log`, including errors. 

*NOTE: If a backup is ever needed to be restored, use the command `tar xvpfz backup.tgz -C /` inside the backup folder. Remember:
- Mount;
- Execute restore script;
- Move out of the directory;
- Unmount.

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

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
    - Select "Ext4 journaling file system".
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

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

### Troubleshooting

The file /etc/resolv.conf is dynamically changing after a system or network service restart. This can cause your browser to not be able to redirect requests. There are ways of working around this. 

1 - You can create a simple script to change the settings to the correct DHCP IP address and run it at every system startup.
2 - Or you can try to force the settings in the network configuration

![image](https://github.com/gustavoalito/BeCode/assets/133368766/a81839ce-1e8c-4595-9d42-2a117aae7f10)

And check the resolv.conf file status: `sudo resolvectl status`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/42d1fcb0-42ad-413a-a04f-c9e5545357f0)

[INDEX](https://github.com/gustavoalito/BeCode/blob/main/Linux-Server-Client-Project/Report.md#index)

---

As long as you have a connection to the outside world and can update packages, you are good to go :)

### Lessons learned

- In Linux, EVERYTHING is a file (quoting Thomas).
- This process takes a lot of time, frustration, perseverance, research, testing, and beer with pizza.
- Don't be afraid to start everything over.
- Be humble, always.
- Don't over-rely on chatGPT. I spent hours working with it trying to figure out my DNS issues. It never helped me much on this specific topic.
- You're always learning.
- Ask for help when you're stuck.
- Help others if you can.
- Exercise, take a break, and sleep well.
- Understand it's a learning experience, don't take it so badly. It's a challenge, and you will defeat it.
- Don't give up, ever!

