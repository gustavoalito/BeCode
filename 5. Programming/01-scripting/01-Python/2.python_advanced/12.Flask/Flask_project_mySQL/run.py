from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from poulette_form import ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b1687609d30bc83eee2868ac748e7d6666f949e5a67f71e8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySQLBOS$!@localhost:3306/flask' # Setting up the DB connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable the modification tracking to avoid warning
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(35), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    message = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    repair = db.Column(db.Boolean, nullable=False)
    order = db.Column(db.Boolean, nullable=False)
    others = db.Column(db.Boolean, nullable=False)

def __init__(self, fullname, email, country, message, gender, repair, order, others):
   self.fullname = fullname
   self.email = email
   self.country = country
   self.message = message
   self.gender = gender
   self.repair = repair
   self.order = order
   self.others = others

# The create_tables() function below is responsible for checking if the tables exist and creating them if they are missing. However, it won't recreate the tables if they are already there, so it's safe to call this function multiple times. When the application starts, it will check the existence of tables and create them if needed.
def create_tables():
    with app.app_context():
        db.create_all()
        print("Database tables created.")

@app.route('/', methods=['GET', 'POST'])
def root():
    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Since the form validation passed, proceed with processing the form data
        fullname = form.fullname.data
        email = form.email.data
        country = form.country.data
        message = form.message.data
        gender = form.gender.data
        repair = form.repair.data
        order = form.order.data
        others = form.others.data

        # Create a new Contact object and save it to the database
        new_contact = Contact(
            fullname=fullname,
            email=email,
            country=country,
            message=message,
            gender=gender,
            repair=repair,
            order=order,
            others=others
        )
        db.session.add(new_contact)
        db.session.commit()

        # Redirect to the result route with the form data
        return redirect(url_for('result', **request.form))

    else:
        return render_template('form.html', form=form, title="Contact Form")
  
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # Process the form data and redirect to the result route with the form data as query parameters
        form = ContactForm(request.form)
        if form.validate_on_submit():
            result = request.form
            json_result = dict(result)
            print(json_result)
            return redirect(url_for('result', **json_result))
        else:
            # If form validation fails, redirect back to the root route
            return redirect(url_for('root'))

    elif request.method == 'GET':
        if request.args:
            # Retrieve the form data from the query parameters in the URL
            result = request.args
            return render_template("result.html", result=result, title="Contact Form Summary")
        else:
            return redirect(url_for('root'))  # If there are no query parameters, redirect to the form page

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

# In the root route, after validating the form data, instead of rendering the result page directly, we redirect the user to the /result route while passing the form data as query parameters in the URL.
# In the result route, we check if there are any query parameters (i.e., the form data) in the URL. If present, we render the result.html template with the provided data. If no query parameters are found, it means the user accessed the /result route directly without submitting the form, so we redirect them back to the form page.