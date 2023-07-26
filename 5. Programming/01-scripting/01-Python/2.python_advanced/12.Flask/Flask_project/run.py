from flask import Flask, render_template, request, redirect, url_for
from poulette_form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b1687609d30bc83eee2868ac748e7d6666f949e5a67f71e8'

@app.route('/', methods=['GET', 'POST'])
def root():
    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Since the form validation passed, proceed with processing the form data
        result = request.form
        json_result = dict(result)
        print(json_result)
        return redirect(url_for('result', **json_result))  # Redirect to the result route with the form data
    else:
        return render_template('form.html', form=form, title="Contact Form")

@app.route('/result', methods=['GET'])
def result():
    if request.args:
        # Retrieve the form data from the query parameters in the URL
        result = request.args
        return render_template("result.html", result=result, title="Contact Form Summary")
    else:
        return redirect(url_for('root'))  # If there are no query parameters, redirect to the form page

if __name__ == '__main__':
    app.run(debug=True)

# In the root route, after validating the form data, instead of rendering the result page directly, we redirect the user to the /result route while passing the form data as query parameters in the URL.
# In the result route, we check if there are any query parameters (i.e., the form data) in the URL. If present, we render the result.html template with the provided data. If no query parameters are found, it means the user accessed the /result route directly without submitting the form, so we redirect them back to the form page.