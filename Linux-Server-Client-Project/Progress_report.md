## PROGRESS REPORT


**1 -

First step was to download the Ubuntu server's ISO file from the official Ubuntu page.
The, when initially installing it via VirtualBox, I used the following pages to help with the steps:

For the Ubuntu server initial install: https://www.youtube.com/watch?v=YtH9D2SqBqA

For the partition, I chose to make it manually. From the free space available, I created a partition of 2GB and mounted it into "mnt/backup".

---

**2 -

Following the link for hardening the server, I installed any packs that were necessary to run the commands I'm used to: 
- plocate (for the "locate" command), 
- net-tools (for the "ifconfig" command) .

The changes in the ssh_config file were the same as the ones from the documentation. 

*SSH-ing from Kali to the server* 

Since the root user in the Ubuntu server is by default disabled, I decided to leave it like this for security reasons. Therefore, I'll test an SSH connection from my Kali to the server using my "boss" user.

The connection is successful.

If I ever need to set the root's password, then I can follow this link: https://www.server-world.info/en/note?os=Ubuntu_22.04&p=initial_conf&f=2

---

**3 -

Install "fail2ban": https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-22-04

Then, configure email: https://technicalramblings.com/blog/how-to-add-email-notifications-to-fail2ban/#adding-the-action => This part didn't work.

---

**4 -

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

