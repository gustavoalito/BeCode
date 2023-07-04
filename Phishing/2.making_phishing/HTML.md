
[Learn HTML_ Elements and Structure Cheatsheet _ Codecademy.pdf](https://github.com/gustavoalito/BeCode/files/11946636/Learn.HTML_.Elements.and.Structure.Cheatsheet._.Codecademy.pdf)

![image](https://github.com/gustavoalito/BeCode/assets/133368766/1789ce5b-eeed-423d-bdbe-5c805dff0da5)

## Forms

To implement a simple form (for learning purposes), I followed this tutorial:
https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form

And I came up with the following basic form (in HTML):

----

<!DOCTYPE html>
<html lang="en-US">
  <head>
    <style>
      form {
        /* Center the form on the page */
        margin: 0 auto;
        width: 400px;
        /* Form outline */
        padding: 1em;
        border: 1px solid #ccc;
        border-radius: 1em;
      }

      div {
        padding: 0;
        margin: 0;
      }

      label {
        /* Uniform size & alignment */
        display: inline-block;
        width: 90px;
        text-align: right;
      }

      input,
      textarea {
        /* Making sure that all text fields have the same font settings. By default, textareas have a monospace font */
        font: 1em sans-serif;

        /* Uniform test field size */
        width: 300px;
        box-sizing: border-box;

        /* Match form field borders */
        border: 1px solid #999;
      }
      
      input:focus,
textarea:focus {
  /* Additional highlight for focused elements */
  border-color: #000;
}

textarea {
  /* Align multiline text fields with their labels */
  vertical-align: top;

  /* Provide space to type some text */
  height: 5em;
}

.button {
  /* Align buttons with the text fields */
  padding-left: 90px; /* same size as the label elements */
}

button {
  /* This extra margin represent roughly the same space as the space
     between the labels and their text fields */
  margin-left: 0.5em;
}
    </style>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
    <form action="/my-handling-form-page" method="post">
      <div>
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="user_name">
        </div>
        <div>
          <label for="mail">Your Email:</label>
          <input type="email" id="mail" name="user_email">
        </div>
        <div>
          <label for="msg">Your Message:</label>
          <textarea id="msg" name="user_message">Type in your message here
          </textarea>
        </div>
        <div class="button">
          <button type="submit">Click here to send your message</button>
        </div>
    </form>
  </body>
</html>

---

![image](https://github.com/gustavoalito/BeCode/assets/133368766/571b03ad-679c-417a-bec9-906aa332b3c0)



Another reference for forms: https://www.w3schools.com/html/html_forms.asp
