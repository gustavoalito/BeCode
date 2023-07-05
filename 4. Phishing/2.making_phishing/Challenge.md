# Challenge

- Bob has a dog (a bull terrier) named "Shimi". Bob really loves his dog. 
- Alice is a fan of Mécanique. She has two vintage cars and often likes to parade around with her ancestral objects.
- Your mission will be to obtain Alice's or Bob's password

---
## Bob

I will focus on Bob's use case since for Alice it would be the same principle, just a change in the page she would visit to register/log in. 

The initial idea was to create a landing page inviting Bull Terrier lovers to register via their Google account. 

It would look something like this:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/e801f10f-4dd2-4a2f-b39a-59d824656901)

The idea was to add the Google login form at the bottom right corner of the page. However, for simplicity reasons, I decided to only create the form. Why is that? Well, the phishing campaign idea would be to:

1. Send a phishing email inviting Bull Terrier lovers to join the website by clicking the provided link.
2. The link would take the users to the Google log in page.
3. Once the users enter their credentials, they would be harvested and send the user back to Google's log in page.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/6bffb91b-2517-4f66-a617-8d35d71f4ced)

You can see the source code in https://github.com/gustavoalito/BeCode/blob/main/Phishing/2.making_phishing/BTB/index.html

Note that the form was cloned from the official Google website. You find the page you want to clone, right-click on it, select "Inspect" and modify the code to your liking and save it on your machine.

Email phishing apart, once Bob clicks the link on the email he received about BTB, he would type in his credentials and submit. What happens next is the following:

## Cedentials Harvesting

I'm using 2 tools on my Kali Linux.

1. SET tool
2. Ngrok

### SET tool

![image](https://github.com/gustavoalito/BeCode/assets/133368766/681ea713-9734-4b9e-ae58-dd5aaa3cef95)

SET stands for Social Engineering Toolkit.

Once you run it, follow the screenshots to make your landing page available. This will create an HTTP server on your localhost, jus tlike we did previously using Nginx and Apache2.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/2122a557-d1f1-46f4-a324-9df2151626cb)
Select **1**

![image](https://github.com/gustavoalito/BeCode/assets/133368766/f292de9a-4f40-49c7-9327-85d8ef5bc4f2)
Select **2**

![image](https://github.com/gustavoalito/BeCode/assets/133368766/d7967b7e-930f-4e6f-9521-a8316995c582)
Select **3**

![image](https://github.com/gustavoalito/BeCode/assets/133368766/bd0dac1d-1379-4c5c-9959-1685212fea37)
Select **3**

The next step will request an IP address to report the POST method back to. If you want to test it only using SET, copy the IP address given at the end of the sentence (it's your IP address). 

Howeve,r for this exercise, we'll use **Ngrok** with SET. This way, we'll have our page server outside of our network, aka to the internet.

Stop here for now and let's move on to Ngrok. 

### Ngrok

Ngrok will serve your wWbb App or page to the internet. Just like you would use python HTTP server. 

- Download it, register to the procduct (it's free) and add your authentication token. All the information can be found here: https://ngrok.com/download

Once set up, open the temrinal and run ngrok `ngrok http 80` => Keep it at port 80 for now, to avoid any confusion with SET. 

![image](https://github.com/gustavoalito/BeCode/assets/133368766/498936d2-4e8c-4f13-a1e8-67bde476caf0)

The **Forwarding** parameter is going to be your IP address on SET. Copy it.

Now, let's go back to **SET**

Paste the Forwarding address from Ngrok to SET, at the point we stopped in SET. If you moved past that point, restart SET, follow the instructions above and you'll surely find your way.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/c924d054-5766-4ad4-85bc-085d8381efc3)

Let's decompose the item from the scrrenshot above:

1. The Forwarding address provided by Ngrok. **This link is also the link the user would receive to click on to register/log in**.
2. The location of the page we will use. In my case, it is located at /home/kali/Documents/BTB. If you want to directly clone a website, you can simply use its address here (for isntance, https://google.com).
3. I chose to copy all the folder's content so my page will render without any broken images. Remembern this is important to look as genuine as possible in a phishing campaign.
4. The page the user will be redirected to after acting on the page you are serving them with. In my case, after th euser submits his credentials, the page will forward him to Google's page.

### Execution

Now, let's test it. Let's suppose we are Bob and we were intrigued by the email we received about this new BTB page. The link will take Bob to the login page, with a cute Bull Terrier image. You will simply type in your Google credentials and submit it. 

You can open the Forwarding link from Ngrok to be redirected to our page.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/87c21dc4-b32e-4f14-8200-c90fb35ae43e)

Once you click *Sign in*, you'll be redirected to Google's landing page.

What happened in the back end?

If oyu check SET, you'll find the credentials logged in it:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/0dc6f4a8-2740-4290-9330-e0da024c4d96)

You have Bob's email address and password.

You can also see it in Ngrok. Click the *Web Interface* link.
![image](https://github.com/gustavoalito/BeCode/assets/133368766/f2c3669f-93b2-4f45-ab1e-b01d002743ae)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/eb3e24db-5be8-45e3-bfd9-316c0e742ef7)

This is basically how you could harvest someones credentials. Obviously, this is a simple example without any URL manipulation. This is only for educational purposes. 

This challenge gives one enough basic knowledge to craft a more persuasive phishing cmapaign.

### Some Reference

- https://www.cybervie.com/blog/phishing-attack-using-kali-linux/
- https://www.youtube.com/watch?v=wXEvK-QmKqQ
- https://getgophish.com/
