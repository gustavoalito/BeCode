# Project: Form in Python with Flask

#### Duration: 5 days
- 1 day to learn about Flask: https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask
  - https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf
  - https://flask.palletsprojects.com/en/2.3.x/quickstart/
  - https://blog.ruanbekker.com/blog/2022/05/31/python-flask-forms-with-jinja-templating/
- 4 days to complete the project.

## Skills developed:
* Backend: PYTHON programming (introduction to logical structures)
* Sanitization and validation of a form
* Implementation of POST and GET methods
* Implementation of templates with Jinja

## Problem statement:
The company Hackers Poulette™ sells DIY kits and accessories for Rasperri Pi. They want to allow their users to contact their technical support. Your mission is to develop a Python script that displays a contact form and processes its response: sanitization, validation, and then sending feedback to the user.

## Performance criteria:
* If the user makes an error, the form should be returned to them with valid responses preserved in their respective input fields.
* Ideally, display error messages near their respective fields.
* The form will perform server-side sanitization and validation.
* If sanitization and validation are successful, a "Thank you for contacting us." page will be displayed, summarizing all the encoded information.
* Implementation of the honeypot anti-spam technique.
  - https://dev.to/felipperegazio/how-to-create-a-simple-honeypot-to-protect-your-web-forms-from-spammers--25n8

#### Form fields
First name & last name + email + country (list) + message + gender (M/F) (Radio box) + 3 possible subjects (Repair, Order, Others) (checkboxes). All fields are mandatory, except for the subject (in this case, the value should be "Others").

## Contact Form (Python)
* Presentation: server/client architecture (transmissive, 10")
* Sanitization: neutralizing any harmful encoding (<script>)
* Validation: mandatory fields + valid email
* Sending + Feedback
* NO NEED FOR JAVASCRIPT OR CSS

#### At the end of this project, you should be able to:
- Explain the difference between a POST request and a GET request.
- Protect yourself against XSS vulnerabilities.
---
Output Encoding:
By default, Jinja2 automatically escapes content placed within {{ ... }} expressions to prevent XSS attacks. I have correctly used this feature in my template. For example, in result.html, where I'm displaying form data in the summary table, the key and value variables are automatically escaped when rendered using {{ ... }}.

Quoted Attributes:
In the provided code, I'm already quoting attributes properly when using Jinja expressions in them. For example, in form.html, all attributes like value="{{ form.fullname() }}", value="{{ form.email() }}", and others are correctly quoted.

Honeypot Trap:
The honeypot trap implemented in form.html is a good technique to catch spam bots without affecting regular users. Since the trap is using Jinja expressions correctly, it doesn't introduce any XSS vulnerability.

Form Input Validation:
In poulette_form.py, I have already implemented some basic form validation using WTForms validators. For example, you have used DataRequired() and Email() validators for the fullname and email fields, respectively. These validators help ensure that the submitted data meets specific criteria.

---
- Protect yourself against SSTI attacks.
---
The code already incorporates good practices like using Flask-WTF for CSRF protection and form validation. The suggested improvement to use the escape filter in result.html further enhances the security by preventing XSS attacks and does not introduce any security issues itself. 

![image](https://github.com/gustavoalito/BeCode/assets/133368766/2909d9ed-ba53-4ddd-a9ef-7f569bc0bc43)

---
- Use a micro framework.
---
Using a micro-framework like Flask is already a good start for building a secure web application due to its lightweight nature and minimalistic approach. 

---
- Perform a deployment.
=======
## SSTI Group Presentation

### Group

Our group consists of myself, [Gokhan](#), [Gustavo](#) and [Mitu](#).

### Subject

We were tasked with the presentation of the SSTI aspect of the project.

### SSTI

Server Side Template Injection, or SSTI is a <ins>template injection attack</ins>.

Templates are files a server uses to render an HTML page and populate it with dynamic data.

Injection attacks are a type of attacks that inject malicious code into your page, usually via form fields and/or urls.

### Detection Phase

As with most attacks, the first step is to figure out wether the target page is vulnerable, for this we will try to inject some logic operations into a field.

Let's use a string that tests most of the common templates, called a polyglot payload.

```${{<%[%'"}}%\.```

If the next step in the form returns an error or raises an exception, the app is vulnerable.

### Identification Phase

Next we need to identify what back-end is running, for this we can decompose the polyglot statement and start injecting specific server language payloads.

![](presentation_img/0_pJf0zn5ChHY9X8sF-1-png-1.png)

After you've identified the backend running on the target, you can start documenting yourself on the possible sandbox-escaping mechanisms and enter the exploitation phase.

### Exploitation Phase
Since the project is in Jinja2, we will take it as an example.

Python being an Object Oriented Programming language, it gives us access to some built-in methods that we could use to exploit the system, such as `__init__`

If we execute this snippet;

```sh
{{ "hello".__class__.__base__.__subclasses__()[182].__init__.__globals__['sys'].modules['os'].popen("ls").read()}}
```
it will run `ls` on the servers filesystem.

To explain what's happening;

![](presentation_img/ssti2.png)

1. Returns the class for the "hello" string, which givse us `<class 'str'>`
2. Returns the base class (parent class that the 'str' class inherits from), it outputs `<class 'object'>`
3. Returns all the child classes inheriting from the 'object' class, which is a list `[<class 'type'>, <class 'weakref'>, ....etc`
4. Returns the class that is located at the index 182, being `<class 'warnings.catch_warnings'>`. We chose this class because it imports the 'sys' module, and from that we can reach the 'os' module.
5. The `__init__` constructor is called and then `__globals__` which returns a dictionary that hold the functions global variables, in this case we need them only for the 'sys' module. Output is `<module 'sys' (built-in)>`
6. 'sys' has many modules built-in, we are only interested in the 'os' one. Outputs `<module 'os' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'>`
7. Any method in the 'os' module can now be invoked, we'll execule `ls` using [popen](https://docs.python.org/3/library/os.html#os.popen) and read the output.

### tplmap
A tool called [tplmap](https://github.com/epinna/tplmap) can be used to help with SSTI attacks.

Once installed, simply run:
```sh
python tplmap.py -u "http://127.0.0.1:5000/?name" --os-shell
```

### Prevention

As for prevention, it's quite straight forward since the attack relies only on your server not being set up proprely and/or accepting dangerous inputs.

<ins>Sanitization</ins>: Input sanitization is a cybersecurity measure of checking, cleaning, and filtering data inputs from users, APIs, and web services of any unwanted characters and strings to prevent the injection of harmful codes into the system.

Flask configures Jinja2 to sanitize output by default.

If your app is required to deal with risky characters (Text editor app, etc...), it is recommended to also Sandbox your environment.

<ins>Sandboxing</ins>: A sandbox is an isolated testing environment that enables users to run programs or open files without affecting the application, system or platform on which they run. 


## Ressources

[Install Flask](https://flask.palletsprojects.com/en/2.3.x/installation/)

[Web Forms in Flask](https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application)

[WTForms](https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf)

[Flask](https://flask.palletsprojects.com/en/2.3.x/)

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)

[Pentester's Guide to Server Side Template Injections](https://www.cobalt.io/blog/a-pentesters-guide-to-server-side-template-injection-ssti)

[Secure Cookie's SSTI writeup](https://secure-cookie.io/attacks/ssti/)

[Secure Cookie's web lab](https://ssti.secure-cookie.io/)

[HackTricks SSTI](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection)
>>>>>>> e87b438e2338ea86ca7651467e46d52ecf6c6ad6
