
from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
import json
import os
# from flask_mail import Mail
# from config import Server
from werkzeug.utils import secure_filename


with open('templates/config.json', 'r') as c:
    params = json.load(c)['params']

local_server = params['local_server']
app = Flask(__name__)
app.secret_key = params["secret_key"]
app.config['Upload_folder'] = params['upload_location']

"""
# Adding mail configurations
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
"""

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = False, nullable = True)
    phone_num = db.Column(db.String(12), unique = False, nullable = False)
    message = db.Column(db.String(1000), unique = False, nullable = True)
    date = db.Column(db.String(12), unique = False, nullable = True)



class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(80), unique = False, nullable = False)
    slug = db.Column(db.String(120), unique = False, nullable = True)
    image_file = db.Column(db.String(30), unique = False, nullable = True)
    content = db.Column(db.String(1000), unique = False, nullable = True)
    date = db.Column(db.String(12), unique = False, nullable = True)
    html_file = db.Column(db.String(120), unique = False, nullable = True)





@app.route('/')
def home():

    posts=Posts.query.filter_by().all()[0:params['posts_in_homepage']]
    return render_template('home.html', params=params, posts=posts)



@app.route('/logout')
def logout():

    session.pop('user')
    return redirect('/dashboard')



@app.route('/delete/post/<string:sno>',methods = ['GET','POST'])
def delete_post(sno):

    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')



@app.route('/delete/message/<string:sno>',methods = ['GET','POST'])
def delete_message(sno):

    if ('user' in session and session['user'] == params['admin_user']):
        message = Contacts.query.filter_by(sno = sno).first()
        db.session.delete(message)
        db.session.commit()
    return redirect('/dashboard')



@app.route('/edit/<string:sno>', methods=['GET','POST'])
def edit_post(sno):

    if ('user' in session and session['user'] == params['admin_user']):
         if request.method == 'POST':
            req_title = request.form.get('title')
            req_slug = request.form.get('slug')
            req_html = request.form.get('html_file')
            req_image = request.form.get('image_file')
            req_content = request.form.get('content')
            date = datetime.now()
            # print(type(sno))
            if sno == '0':
                rows = db.session.query(Posts).count()
                post = Posts(sno = (rows + 1),
                             title = req_title,
                             date = date,
                             slug = req_slug,
                             html_file = req_html,
                             image_file = req_image,
                             content = req_content)
                db.session.add(post)
                db.session.commit()
                flash('New Post Added Successful.')
                return redirect('/dashboard')
            else:
                post = Posts.query.filter_by(sno = sno).first()
                post.title = req_title
                post.date = date
                post.slug = req_slug
                post.html_file = req_html
                post.image_file = req_image
                post.content = req_content
                db.session.commit()
                flash('Edited Post Saved successful.')
                return redirect('/edit/' + sno)
         post = Posts.query.filter_by(sno = sno).first()
         return render_template('edit.html', params = params, sno = int(sno), post = post)



@app.route('/uploader', methods = ['GET','POST'])
def file_upload():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['Upload_folder'], secure_filename(f.filename)))
            return "Uploaded Sucessfull"



@app.route('/message/<string:sno>', methods=['GET','POST'])
def read_message(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        #if request.method == 'POST':
        #req_title = request.form.get('title')
        contact = Contacts.query.filter_by(sno=sno).first()
        return render_template('message.html', params = params, contact = contact, sno = sno)



@app.route('/dashboard', methods = ['GET','POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        contacts = Contacts.query.all()
        return render_template('dashboard.html', params = params, posts = posts, contacts = contacts)
    if request.method == 'POST':
        username = request.form.get('admin_name')
        password = request.form.get('admin_password')
        if username == params['admin_user'] and password == params['admin_password']:
            #set the session variable
            session['user'] = username
            posts = Posts.query.all()
            contacts = Contacts.query.all()
            return render_template('dashboard.html', params = params, posts = posts, contacts = contacts)
    else:
        return render_template('login.html', params = params)



# @app.route('/blog')
# def music():
#     return render_template('blog.html', params=params)



@app.route('/about')
def about():

    return render_template('about.html', params = params)



@app.route('/signin')
def signin():

    return render_template('login.html', params = params)



@app.route('/contact', methods = ['GET', 'POST'])
def contact():

    if request.method == 'POST' :
        # ADD ENTRY TO DATABASE
        name = request.form.get("name")
        email = request.form.get("email")
        contact_num = request.form.get("phone")
        text = request.form.get("textarea")

        rows = db.session.query(Contacts).count()
        entry = Contacts(sno = (rows + 1),
                         name = name,
                         email = email, 
                         phone_num = contact_num,
                         date = datetime.now(), 
                         message = text)
        db.session.add(entry)
        db.session.commit()
        flash('Your Message has been sent Successful.')
        """mail.send_message('New mail from' + name,
                          sender = email, 
                          recipients = [params['gmail_user']],
                          body = text + "\n" + contact_num)"""

    return render_template('contact.html', params = params)
    #return {"name":name,
    #        "email":email
    #}



@app.route('/post/<string:post_slug>', methods = ['GET'])
def post_page(post_slug):

    #post= Posts.query.filter_by(slug=post_slug)
    post= Posts.query.filter_by(slug=post_slug).first()
    
    if ".html" not in post.html_file:
        print(post.html_file)
        return redirect(post.html_file, code=302)
    else:
        return render_template(post.html_file, params = params, post = post)
    # return render_template(post.html_file, params=params, post=post)





if __name__ == '__main__':
    app.run(debug = True)
