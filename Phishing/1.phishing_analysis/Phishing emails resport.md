# Phishing Analysis Report


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

## Email 1

### Email timestamp
20/03/2023 16:57

### Who is the email from?

Paypal Belgium

### What is the sender's email address?

![image](https://github.com/gustavoalito/BeCode/assets/133368766/1ea7e4d1-8d60-4811-839b-d8060cb398d7)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/8911d78a-ecc9-4f46-84a6-1073c71e70bd)

According to Paypal Belgian's page on phishing, a valid Belgian PayPal address contains the domain name PayPal.be.
Ref.: https://www.paypal.com/be/webapps/mpp/phishing

### What email address will receive a reply to this email? 

Return-Path: service@paypal.be

### What brand was this email tailored to impersonate?

Paypal

### What is the originating IP? Defang the IP address.

66[.]211[.]170[.]87

![image](https://github.com/gustavoalito/BeCode/assets/133368766/14fa9b51-12f2-4422-9a3b-7810698a9ab1)

### Domain of interest

paypal[.]com

### Shortened URL(s)

hxxps[://]www[.]paypalobjects[.]com/digitalassets/c/system-trig=
hxxps[://]www[.]paypalobjects[.]com/digitalassets/c/system-trigger=
hxxps[://]www[.]paypalobjects[.]com/digitalassets/c/system-triggered=
hxxps[://]www[.]paypal[.]com/cgp/app-redirect?intent=3Dxo_email_txn_details&a=
hxxps[://]www[.]paypal[.]com/cgp/app-redirect?intent=3Dx=
hxxps[://]www[.]paypal[.]com/be/webapps/mpp/paypal-buyer-protection?v=3D1&amp=
hxxps[://]www[.]paypalobjects[.]com/digitalassets/c/system-triggered-email/n/=
hxxps[://]www[.]paypal[.]com/be/smarthelp/home?v=3D1&amp;utm_source=3Dunp&amp;utm_m=
hxxps[://]www[.]paypal[.]com/be/webapp=
hxxps[://]www[.]paypal[.]com/be/webapps/mpp/mobile=
hxxps[://]twitter[.]com/PayPal?v=3D1%2C0[.]1=
hxxps[://]www[.]paypalobjects[.]com/digitalassets/c/system-triggere=
hxxps[://]www[.]instagram[.]com/paypal/?v=
hxxps[://]www[.]paypalobjects[.]com/digitalassets/c/system=
hxxps[://]www[.]facebook[.]com/PayPalUSA?v=
hxxp[://]www[.]linkedin[.]com/company/1482?=
hxxps[://]www[.]paypalobjects[.]com/digitalasset=
hxxps[://]www[.]paypal[.]com/us/webapps/mpp/security/suspicious-act=
hxxps[://]www[.]paypal[.]com/selfhelp/h=
hxxps[://]www[.]paypal[.]com/be/smarthelp/article/why-am=
hxxps[://]t[.]paypal[.]com/ts?v=3D1&amp;utm_source=

### Verdict

![image](https://github.com/gustavoalito/BeCode/assets/133368766/eb8b1c4f-b629-4983-8a18-a6de3ed91e94)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/341c2d06-15fa-4f34-a55d-91e4b6621d40)

This looks like a legitimate email, not a phishing one. The sender's email address corresponds to the official Belgian Paypal domain. Moreover, the links of the action buttons point to the Paypal.com domain.

The originating IP address belongs to Paypal.
![image](https://github.com/gustavoalito/BeCode/assets/133368766/12b944bc-d74c-4960-8e62-567826c5f508)


The links in the source code point to Paypal, and the social media links do resolve to Paypal's account on those platforms. Some links are no longer available. 

![image](https://github.com/gustavoalito/BeCode/assets/133368766/06684d77-a0d6-4190-a146-421f873780bf)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/2addd6c4-91be-43ca-8f05-0a977a47001c)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/e598c187-a36b-4f32-b63b-ceb337aa6cfa)

A couple of link verification, and no phishing reported on those links:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/d3cf883f-40d4-4a24-83c4-e10a62124f03)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/76ac3028-0c62-4e7a-9134-4ae2aa9ab152)
![image](https://github.com/gustavoalito/BeCode/assets/133368766/c2496d39-0e1d-4f6d-879f-e29145e0df02)

### Tools used

- https://www.virustotal.com
- https://mxtoolbox.com
- https://phishtank.com
- CyberChef (https://gchq.github.io/CyberChef
