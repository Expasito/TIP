from root import app
from flask import render_template
@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html',name="Expasito")

@app.route('/fileone')
def fileone():
    test_users=("Expasito","Sam","George","Steve")
    return render_template('pageone.html',users=test_users,num=len(test_users))

@app.route('/filetwo')
def filetwo():
    test_posts=("Hello","Hi","TestOne","TestTwo")
    return render_template('pagetwo.html', posts=test_posts)
