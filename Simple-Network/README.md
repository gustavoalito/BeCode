# Building a simple network

# Executive Summary

The inter network infrastructure built using Cisco Packet Tracer for Hackers Poulette is comprised of:
- 3 PCs running Win10,
- A printer,
- A DNS server,
- A Switch (Model 2960 IOS15) to connect all the PCs, printer and server,
- A Router (Model ISR4331) to manage traffic from the intra network to the Internet (and vice versa),
- 6 ethernet cables.

> Note that the structure is divided into 3 networks, to help understanding the concept of networking. Therefore, we have 3 distinct networks in this project. To help us emulate the internet, we are connecting the intranet to the outside world.
The outside world is represented by NETWORK 3. 
NETWORK 2 is the representation of the intranet's router connecting to the outside world. The connecting router on the other side, is an entry point to the internet.

# Intranet Network Description

|Devices|IP Address|Mask|Default Gateway|DNS Server|
|---|---|---|---|---|
|PC-Robert|192.168.1.10|255.255255.0|192.168.1.1|192.168.1.254|
|PC-Camille|192.168.1.11|255.255255.0|192.168.1.1|192.168.1.254|
|PC-Renaud|192.168.1.12|255.255.255.0|192.168.1.1|192.168.1.254|
|Printer|192.168.1.13|255.255.255.0|192.168.1.1|192.168.1.254|
|DNS server|192.168.1.254|255.255.255.0|192.168.1.1|192.168.1.254|

## In between networks (NETWORK 2)

Network 2 is a network composed of the intranet router's interface connecting to the outside world and another router simulating the entry point to the internet. The connection between them both is also considered a network.

Intranet Router's IP address: *192.168.2.1*
Extranet Router's IP address: *192.168.2.2*

A route is configured between both routers so they can see each other and know how to direct traffic between them.

|Router|Target Network|Via|
|---|---|---|
|Intranet|192.169.1.0|Extranet Router|
|Extranet|192.168.1.0|intranet Router|

## NETWORK 3

Network 3 is simulating the outside world, aka, the internet. It is comprised of a Web server connecting to the internet via its interface represented as the Extranet Router. 

# Simulating the Internet

In order to simulate the internet, the DNS server (NETWORK 1) and the Web server (NETWORK 3) are used. Basically, all devices are configured with the DNS server's IP address (192.168.1.254). This means that, for this purpose, the users utilizing their web browser will send a HTTP request to the DNS server, who in turn will translate the requested page to its IP address and redirect the request to it.

The request arrives then to the machine hosting the web page. In this case, it is the Web server (192.169.1.2).

For illustration purposes, the page we will simulate is www.ss.com.

Robert, who is a lifetime fan of Steven Seagal, wants to check his favorite actor's page for any news on him. He opens his web browser and types www.ss.com.

Let's see what happens next:
- The HTTP request from Robert's PC is sent to the DNS server,
- The DNS server receives the request and checks its table. It is recorded that the address requested (www.ss.com) translates to the IP address 192.169.1.2,
- The DNS server send the request to the IP address. The request travels through the intranet router and reaches NETWORK 3,
- The Web server receives the request and, in turn, replies with the web page data to be displayed on Robert's screen. The data travels back to NETWORK 1,
- The data is received by Robert's PC and the page is rendered for him,
- Robert is happy :)
 

# Wrapping up

The hosts (PCs) are all connected to a switch. The switch manages the communication among the PCs. Then, the switch on its turn is connected to an outside router. The router is used to manage the communication between 2 or more networks.

Hosts are all operational within the 3 networks and are connected to the internet via their intranet router. This star network topology supports fast scability.

Internet is simulated via a web page hosted in the Web server. The web page's IP address is stored in the DNS server's table. The DNS server forwards the HTTP request to the Web server. The Web server, in tur,, send the requested data to the initial requester.
