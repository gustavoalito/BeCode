# Email 2 - Phishing Analysis Report


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

Mon, 12 Dec 2022 03:56:38 -0500 or Mon, 12 Dec 2022 09:56:36 +0100


### Who is the email from?

Supposedly from Trustwallet.com.

### What is the sender's email address?

A "no reply" account: `From: "noreply" <stainless@midnightmagicevents.com>`
![image](https://github.com/gustavoalito/BeCode/assets/133368766/c4b269e5-f9ff-43d7-90dd-8aaa9b03f892)

### What email address will receive a reply to this email? 

The same as the sender's: `Reply-To: stainless@midnightmagicevents.com`

### What brand was this email tailored to impersonate?

Trust Wallet

### What is the originating IP? Defang the IP address.

85[.]209[.]134[.]107

From the NL
![image](https://github.com/gustavoalito/BeCode/assets/133368766/856be2a6-bafe-4367-8a99-6b83452a9071)

Whereas the real trustwallet.com domain is registered and served in the US:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/ad39df00-1f4a-4dca-b10b-a53f3d2f248a)


### Domain of interest

trustwallet.com

### Shortened URL(s)

hxxps[://]trustwallet[.]com
hxxps[://]climovil[.]com

### Verdict

This is phishing - a lousy one.

The rendered email takes Trust Wallet's logo. There is no typo. The sense of urgency demands the user verify their account, otherwise, it will be suspended. 

There are no malicious attachments or links. The only action the user can take (except answering the email). The link is to a legitimate climatization business: `https://climovil.com`. 
![image](https://github.com/gustavoalito/BeCode/assets/133368766/c6fe597f-82e4-47eb-96ee-37766c361c18)


This email brings no harm if the link provided is clicked. It just redirects the users to a site they were not expecting to visit. The only risk can be to reply to the email and provide credentials if requested. Therefore, THERE IS a risk.

### Tools used

- https://www.virustotal.com
- https://mxtoolbox.com
- https://phishtank.com
- CyberChef (https://gchq.github.io/CyberChef
- https://www.whois.com
- https://app.phishtool.com/
