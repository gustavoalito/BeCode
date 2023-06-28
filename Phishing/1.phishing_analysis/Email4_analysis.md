# Email 4 - Phishing Analysis Report


**Generally speaking, I aim at answering the following questions:**

- What is the email's timestamp? 
- Who is the email from?
- What is the sender's email address?
- What email address will receive a reply to this email? 
- What brand was this email tailored to impersonate?
- What is the originating IP? Defang the IP address. 
- What do you think will be a domain of interest? Defang the domain.
- What is the shortened URL? Defang the URL.
- Tools used

---

## General considerations

When it comes to phishing - just like everything in life - if something looks too good to be true, that's probably because it is.

Secondly, use common sense. 

This email in question is not hiding links or trying to steal users' confidential information. This is a scam that will lure the victim into paying some amount of money in the hopes of getting rewarded with a high amount of money.

### Email timestamp

`Fri, 3 Mar 2023 12:44:01 +0100`

### Who is the email from?

Dr. Dan Miller, the United Nations Special Representative for Disaster Risk Reduction (UNDRR).

### What is the sender's email address?

`"Dr. Dan Miller" <babakingsouthmichael@gmail.com>`

### What email address will receive a reply to this email? 

`Reply-To: imorourafiatou0@gmail.com`

### What brand was this email tailored to impersonate?

United Nations

### What is the originating IP? Defang the IP address.

209[.]85[.]220[.]41

### Domain of interest

`un.org`

### Shortened URL(s)

None found.

### Verdict

Ask yourself these questions:

- Does an organization like the UN (and IMF) give out relief payments like that, by email to random people? How nice of them...
- Should a UN representative use a Gmail account? Why doesn't he use his official UN email account? This would look more authentic.
- Why me? Look at the email header:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/83ffc3cc-e0b2-4a15-9742-a413b2c6bc96)

The email starts as if it was a reply. Then, your email address is in BCC (Blind Carbon Copy), not even the one and only recipient (considering the importance of this business). Then, the person you are requested to contact is located in Benin:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/4f758e95-a67a-43f0-80a5-af1c8b27f3ed)

Do you even know where Benin is? 

Well, at least there are UN agencies there:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/b919f4d4-da7e-40b3-962b-fd5af7778649)

Checking the sender's IP address resolves to a Google domain.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/75acca89-069e-4236-94ba-f60af52a309f)

One can interact with this email, for fun and research outcomes. As long as no money and personal information is shared...
Just do it like this: https://www.youtube.com/watch?v=4o5hSxvN_-s

### Tools used

- Common sense
- CyberChef (https://gchq.github.io/CyberChef
- https://www.whois.com
- https://app.phishtool.com
