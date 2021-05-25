from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail

with open('templates/config.json', 'r') as c:
    params = json.load(c)['params']

local_server = True
app = Flask(__name__)
app.secret_key = "super secret key"#change this to more suitable value
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_DEBUG = app.debug,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password'],
    DEFAULT_MAIL_SENDER = None

)
mail=Mail(app)
#'mysql://username:password@localhost/db_name'
if local_server:
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sblog'
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), unique=False, nullable=False)
    email= db.Column(db.String(120), unique=False, nullable=True)
    phone_num= db.Column(db.String(12), unique=False, nullable=False)
    message= db.Column(db.String(1000), unique=False, nullable=True)
    date= db.Column(db.String(12), unique=False, nullable=True)

class Posts(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80), unique=False, nullable=False)
    slug= db.Column(db.String(120), unique=False, nullable=True)
    image_file= db.Column(db.String(30), unique=False, nullable=True)
    content= db.Column(db.String(1000), unique=False, nullable=True)
    date= db.Column(db.String(12), unique=False, nullable=True)


#<input type="submit" value="Send">
@app.route('/')
def home():
    posts=Posts.query.filter_by().all()[0:params['posts_in_homepage']]
    return render_template('home.html', params=params, posts=posts)

@app.route('/dashboard')
def dashboard():
    return render_template('login.html', params=params)


@app.route('/blog')
def music():
    return render_template('travel.html', params=params)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/signin')
def signin():
    return render_template('login.html', params=params)

@app.route('/codes')
def codes():
    return render_template('codes.html', params=params)


@app.route('/contact', methods =['GET', 'POST'])
def contact():
    if request.method=='POST' :
        # ADD ENTRY TO DATABASE
        name = request.form.get("Name")
        email = request.form.get("Email")
        contact_num = request.form.get("Phone")
        text = request.form.get("textarea")

        #entry = Contacts(name=name, email=email, phone_num=contact_num,date=datetime.now(), message=text)
        #db.session.add(entry)
        #db.session.commit()
        
        """mail.send_message('New mail from' + name,
                          sender = email, 
                          recipients = [params['gmail_user']],
                          body = text + "\n" + contact_num)"""

    return render_template('contact.html', params=params)
    #return {"name":name,
    #        "email":email
    #}

@app.route('/post/<string:post_slug>', methods=['GET'])
def post_page(post_slug):
    #post= Posts.query.filter_by(slug=post_slug)
    post= Posts.query.filter_by(slug=post_slug).first()
    return render_template('post101.html', params=params, post=post)

app.run(debug=True)


#if tagline, blog name chnage krna hai to use {{params['tag_line']}} type of text in html file
#config file me add kr dena names and value




"""
Requirements:
pip install mysql-connector-python
pip install flask_sqlalchemy
pip install flask
pip install flask_mail
pip install mysqlclient
"""