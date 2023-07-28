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
