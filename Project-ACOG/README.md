# Project ACOG
This network building exercise was completed as a group project named Project ACOG by our team. We successfully presented our project to the class and explained step by step how we set up our network.

## Contributors

* Nomade73
* Gustavo 
* Olga
* Alejandr0-1

## Components

For the local network:

*  1 Router (named RouterHQ)
*  1 Switch L3 
*  3 servers (DNS,DHCP, TFTP)
*  10 switch (1 switch for each departement except support)
*  3 sectors :
*     Production : 10 posts
*     Secretariat : 5 posts
*     Study : 8 posts
*  2 support sectors (each with 30 posts) each sectors divided into 3 subsectors with 10 posts each

## Additionnal Components :
* External Router (RouterVPN) with IP 192.168.100.254 255.255.255.0 connected to Study Sector
* a DMZ with 1 firewall ASA, 1 router and 1 server
* 1 Cloud

---

## How to setup DHCP services with VLAN

> STEP 1 : CREATE, ASSIGN IP/SUBNET MASK FOR VLANS

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/d74ffd61-20db-469e-b6c4-42dab8efa760)


> STEP 2 : CONFIGURE DHCP SERVER

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/3c8e93c8-0dbf-4158-9f66-f2536a086762)

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/aa7b552b-e28f-4887-99cd-7c60f9d44b62)

> STEP 3 : CONFIGURE MODE ACCESS/TRUNK IN VLANS

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/33d6e2c1-de97-48ca-b527-189c5919dd20)
![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/e654c590-c30e-4c65-94d9-1d397a371ab0)


> STEP 4 : TELL PC IN VLANS WHERE TO GET IP

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/97d36cf4-70b9-4d19-a089-695dcda3364e)


> STEP 5 : ROUTING FOR MULTILAYER SWITCH

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/b0309c97-d438-43d3-8218-7aff219a7491)


(if you forgot this step, you can not ping between two VLANs, first packet which ping from one VLAN to another VLAN will fail => because it needs time to find out path => timed out.

> STEP 6 : CHECK

## How to setup a DNS server with VLANs

Adding a DNS server starts with selecting a general server and adding it into the desired cluster. Then, for the sake of simplicity, we’ll assign a static IP address to it.

The DNS server is in the same cluster as the DHCP and FTP and we assigned the IP address of 192.168.30.1 to it.

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/db8f80f8-3d3b-4e0b-8e2a-171d8453b92e)


**NOTE**: To save time, it’s preferable to have an assigned IP address to the DNS server when configuring the DHCP. This way the DNS’ IP address is already inputted in the DHCP server configuration. This ensures that all PCs benefiting from a dynamic IP address from the DHCP server also receives the DNS server’s IP address.

To configure the DNS server, open the server’s options screen > Services > DNS.

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/bb0634a0-c4f8-4f5a-954a-076ec1648dc5)


First, turn it on. We’ll then create 3 different records with different IP addresses assigned to them to demonstrate that the DNS will receive 3 different requests and will translate them into their corresponding IP addresses.

For the demonstration purposes, any PC user trying to open the “dhcp” web page will send his/her request to the DNS server, who, in turn, will redirect the request to the IP address 192.168.30.2. 

The way this works is simple. You add the page that users will try to connect to. This is the “Name”. The Address field is the IP address of the server containing the page itself. 

See the table below for a summary of the page and the way they work:

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/69b72982-506d-4c1e-bfcf-a100e690b59b)


Now that we have mapped where each page will be hosted, we can customize the index.html page of each page just to make it more identifiable.

### DNS Server (192.168.30.1)

Let’s take the example of the DNS server’s page. Every user trying to connect to its page, dns, will reach the index.html page hosted in 192.168.30.1.

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/c78be718-868f-4b40-8856-b4cd405729da)


Instead of configuring the DNS part of it, we will configure the HTTP part.

We go to item 5, index.html and click the (edit) button.

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/109217cc-8b7b-4d42-b531-e1cb1a139dc6)


There we can customize the text of the page. For this example, we only added the last line “this a dns” to be able to identify it. Make sure to click the save button at the top right of the window once you have finished.

Let’s go to a PC, open its web browser and type “dns” there and see what happens.

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/112e24e6-d097-4eb6-bc9c-4fe2d267f30d)


Success!

Now, we’ll do the same for the other 2 servers and test it.

### DHCP server (192.168.30.2)

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/99d9ef35-6235-47f5-980b-8f9e0f4d2632)
![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/d85054a1-b2e9-410b-b13d-34c79d9b89e2)


Test result by opening a web browser page of a random PC and typing “dhcp”:

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/5573160d-25c6-44e6-bf8a-77a12723393c)


Success!

Now, we’ll do the same for the last server and test it. 

### FTP server (192.168.30.3)

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/80a5345c-7687-4641-9301-ae4170572643)
![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/98dca285-7d77-4419-9e38-2b26776c294d)


Test result by opening a web browser page of a random PC and typing “web”:

![image](https://github.com/Nomade73/BecodeBrussels/assets/133368766/29698409-fdf3-4db8-b3fd-a5fc08c7e058)


Success! Don’t mind the text as we used the FTP server to act as a web server, but just for this test.

### SSH

You can enable SSH on a Cisco device by entering the global configuration mode using the command "configure terminal".

Generate an RSA key pair for SSH authentication using the "crypto key generate rsa" command. Choose the key size (e.g., 1024 or 2048 bits) and confirm the key generation.

Configure the device's hostname using the "hostname" command. This step is necessary for SSH authentication.

Create a user account with privilege level and password using the "username" command.

Finally, enable SSH login using the "line vty" command to access the virtual terminal lines, and specify the transport input as SSH.


# Building VLAN's
# Step 1: **Determine VLAN Requirements**

As a first step in our project we had to identified the purpose of VLANs, 
such as separating departments, isolating traffic, or enhancing security.

# Step 2: **Plan the VLAN Configuration**

We determineted the VLAN IDs (VLAN tags) for each VLAN. These are numeric identifiers used to identify VLANs.
After we decided whether to use static VLANs (manually assigned) or dynamic VLANs (assigned based on protocols like VLAN Trunking Protocol - VTP).
In the end of this step we planned the IP addressing scheme for each VLAN if it included routing.

# Step 3: **Configure Switch Ports**

For configure switch ports we accessed the management interface of the network switch (via web interface or command-line interface).
For each VLAN, we configureted the switch ports to be members of that VLAN.
We assined the appropriate VLAN ID to each port.
The last things to do in this step was:
-Set the port mode to access mode for devices connecting to the VLAN.
-Set the port mode to trunk mode for interconnecting switches or routers.

# Step 4: **Create VLANs on the Switch**

We had to again access the switch's management interface and then 
navigate to the VLAN configuration section.
Next step was create VLANs using the desired VLAN IDs from the earlier plan
and assign a name to each VLAN for identification.

# Step 5: **Configure VLAN Interfaces (Optional)**

For routing between VLANs, we configureted VLAN interfaces on a Layer 3 switch or a router and
assigned IP addresses to the VLAN interfaces, following the IP addressing scheme you planned.

# Step 6: **Test and Verify**

At the end we connected devices to the appropriate switch ports assigned to each VLAN.
Is important to verify connectivity and ensure that devices within the same VLAN 
can communicate while being isolated from devices in other VLANs.

*Test inter-VLAN routing if configured.*