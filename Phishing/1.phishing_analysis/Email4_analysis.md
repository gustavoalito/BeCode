# Email 3 - Phishing Analysis Report


**Generally speaking, I aim at answering the following questions:**

- What is the email's timestamp? 
- Who is the email from?
- What is the sender's email address?
- What email address will receive a reply to this email? 
- What brand was this email tailored to impersonate?
- What is the originating IP? Defang the IP address. 
- What do you think will be a domain of interest? Defang the domain.
- What is the shortened URL? Defang the URL.
- Verdict
- Tools used

---

### Email timestamp

Sun, 26 Mar 2023 13:31:56 +0000

### Who is the email from?

Tinder

### What is the sender's email address?

`Tinder <gq@80-78-255-128.cloudvps.regruhosting.ru>`

### What email address will receive a reply to this email? 

The same: 
`Return-Path: gq@80-78-255-128.cloudvps.regruhosting.ru`

### What brand was this email tailored to impersonate?

Tinder

### What is the originating IP? Defang the IP address.

80[.]78[.]255[.]128

### Domain of interest

tinder.com

### Shortened URL(s)

hxxp[://]www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional[.]dtd
hxxp[://]www[.]w3[.]org/1999/xhtml
hxxps[://]fonts[.]googleapis[.]com/css?family=Montserrat:400,400i,700,700i,900,900i
hxxps[://]marketing-images[.]gotinder[.]com/3d7c06f59dcf45558d19d0e284c88091/0[.]jpg
hxxp[://]blog[.]tulingxueyuan[.]cn/contradictedqm[.]php?utm_campaign=tpdjuresn
hxxps[://]marketing-images[.]gotinder[.]com/f91fd4489df8488c988705a3a43c80e1/0[.]png
hxxps[://]marketing-images[.]gotinder[.]com/06537a2d608c459699cc8a63a188e167/2[.]png
hxxps[://]marketing-images[.]gotinder[.]com/06537a2d608c459699cc8a63a188e167/3[.]png
hxxps[://]marketing-images[.]gotinder[.]com/dfbeff40885e4192bea8da73c5c8e550/0[.]png

### Verdict

This is phishing. It is a well-crafted email, though. 

- The 1st indication of phishing is the sender's email address, which starts with `gq@` and the domain is composed of its IP address followed by the domain name and `.ru`. This does not look at all as a legitimate Tinder email address.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/35ee3d90-e9ee-4826-be13-c58ae1212aa8)

- The 2nd indication is the suspicious link (a Chinese blog?) when you hover over the button "FIND OUT WHO":
![image](https://github.com/gustavoalito/BeCode/assets/133368766/efb9ce78-fd9e-4a72-8daf-a1dd1ca4b458)

The same link is used for the other links in the email:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/0edac223-ed67-45ac-a7be-66694d821bcb)

However, it is no longer an active link:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/9899cda7-162f-4637-86f9-6242724ac1c2)

This link is reported by different tools that it is a malicious link:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/b1336620-614c-44d0-9bf6-93867e737786)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/58feeec0-c4fd-462f-b5b6-594cff3aa6d3)

The sender's IP address is from Russia:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/56f57b16-a732-4367-a695-ab3c3a0b90d0)


### Tools used

- https://www.virustotal.com
- https://mxtoolbox.com
- https://phishtank.com
- CyberChef (https://gchq.github.io/CyberChef
- https://www.whois.com
- https://app.phishtool.com
