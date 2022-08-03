from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

#magic lines start here
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

Config = {"apiKey": "AIzaSyAKuPVfWd4FU9MPxI19lSREeIs2LDJI3hY",
"authDomain": "cs-personal-project-56a1b.firebaseapp.com",
"projectId": "cs-personal-project-56a1b",
"storageBucket": "cs-personal-project-56a1b.appspot.com",
"messagingSenderId": "494172566669",
"appId": "1:494172566669:web:89ba5e3cbe103244cf1ec4",
"measurementId": "G-VNP1PDBGRE",
"databaseURL": "https://cs-personal-project-56a1b-default-rtdb.europe-west1.firebasedatabase.app/"}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
#magic lines end here


#Code goes below here


#basic signs down here
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user= {"Name":request.form['fullname'], "Username": request.form['username']}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('home'))
        except:
            print("Error, identification failed. Please try again.")
    return render_template("signup.html")


@app.route('/', methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            print("Error, identification failed. Please try again.")
    return render_template("signin.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))

@app.route('/home')
def home():
    return render_template('home.html')
#basic signs end here


@app.route('/recipes', methods = ['GET', 'POST'])
def recipe_submit():
    return render_template('recipes.html')



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)