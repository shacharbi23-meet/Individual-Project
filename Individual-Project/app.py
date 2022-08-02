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
"measurementId": "G-VNP1PDBGRE"
"databaseURL": "https://cs-personal-project-56a1b-default-rtdb.europe-west1.firebasedatabase.app/"}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
#magic lines end here



#Code goes below here




#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)