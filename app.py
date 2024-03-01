
# importing libraries and some functoins

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ecommerce.db"           
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Set a secret key for sessions



db = SQLAlchemy(app)

# initializing database
class Ecommerce(db.Model):
    inputEmail14 = db.Column(db.String(200), primary_key=True)
    inputPassword4 = db.Column(db.String(500), nullable=False)
    inputAddress = db.Column(db.String(500), nullable=False)
    inputAddress2 = db.Column(db.String(500), nullable=False)
    inputCity = db.Column(db.String(500), nullable=False)
    inputState = db.Column(db.String(500), nullable=False)
    inputZip = db.Column(db.String(500), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.inputEmail14}"


# verify password function for wrong password
def verify_password(inputPassword4, password):
    print("we are here in vberify")
    salt = inputPassword4[:32]
    # hashed_input_password = hashlib.sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    print("we are here in vberify")
    return  inputPassword4==password


# front_1 which redirect the user to front page
@app.route('/')
def front_1():
    return redirect(url_for('front'))

# # front which redirect the user to front page

@app.route('/front')
def front():
    return render_template('front.html')

# # login fuction which first get the details of the user with the help of get method and the reply in term of post method will come,
# and then with if statement it compares to post if incoming details are correct then it will further started to match the details 
# then using verify password function if user entering right information it redirects to the account page.



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        inputEmail1444 = request.form['inputEmail144']
        inputPassword444 = request.form['inputPassword44']

        ecommerce = Ecommerce.query.filter_by(inputEmail14=inputEmail1444).first()

        if ecommerce and verify_password(ecommerce.inputPassword4, inputPassword444):
            session['user_id'] = ecommerce.inputEmail14
            return redirect('/account.html')
        else:
                        # Flash a message
            flash('Invalid credentials'," ")
            # Render the login page with the error message
            return render_template('login.html')


    return render_template('login.html')



# accountfunction which redirect the user to accountpage
@app.route('/account.html')
def account():
    return render_template('account.html')



# menCatalogue function  which redirect the user to menCatalogue
@app.route('/menCatalogue')
def menCatalogue():
    
    return render_template('menCatalogue.html')  
# WomenCatalogue function  which redirect the user to WomenCatalogue
@app.route('/womenCatalogue')
def womenCatalogue():
   
    return render_template('womenCatalogue.html')  

#about function which redirect the user to about page
@app.route('/about')
def about():
    
    return render_template('about.html')


# signUp function which redirect the user to signUp page after getting all details of user and adding them into the database of our system
@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        inputEmail14 = request.form['inputEmail4']
        inputPassword4 = request.form['inputPassword4']
        inputAddress = request.form['inputAddress']
        inputAddress2 = request.form['inputAddress2']
        inputCity = request.form['inputCity']
        inputState = request.form['inputState']
        inputZip = request.form['inputZip']

  

        ecommerce = Ecommerce(
            inputEmail14=inputEmail14,
            inputPassword4=inputPassword4,  
            inputAddress=inputAddress,
            inputAddress2=inputAddress2,
            inputCity=inputCity,
            inputState=inputState,
            inputZip=inputZip
        )

        db.session.add(ecommerce)
        db.session.commit()

        return render_template('signUp.html', message='Sign up successful')

    return render_template('signUp.html')



if __name__ == "__main__":
    app.run(debug=True, port=7000)


