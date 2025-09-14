from flask import Flask, url_for, request, send_file, abort
from flask import render_template,flash,redirect
from app import app
from app.forms import LoginForm

"""
    Description file: Function RoutesApp mit Flask und ansehen/view
    Data:
            #app.run(host,port,debug, options)
            #host - 127.0.0.1 (default localhost)
            #host - '0.0.0.1' (alle horen )
            #port = 5000
    
    command:
            export FLASK_APP=app.py        
            for test:
                http://127.0.0.1:5000/login?name=Ruslan
                http://127.0.0.1:5000/path1/

    Author:     RuslanLisovenko@gmail.com
    Date:       0804-2024
"""   
#---------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():       
    myform = LoginForm(csrf_enabled=False)
    if myform.validate_on_submit():
        flash('Enter request for user {}, write= {}'.format(myform.username.data, myform.remember_me))
        return redirect('/index')
    return render_template('login.html', title = 'Enter', form = myform)

@app.route('/')
@app.route('/index')
def start_page():    
    user = {'username' : 'Ruslan'}

    posts = [
            {
                'author' :{'username' : 'Ruslan'} ,
                'body'   : 'Hallo!'
            },
            {
                'author' :{'username' : 'Jurgen'} ,
                'body'   : 'Hallo Jurgen!'
            },
            {
                'author' :{'username' : 'Viktor'} ,
                'body'   : 'Hallo Viktor!'
            }
    ]
    return render_template('index.html', title = 'Home page', user = user, posts=posts)
#---------------------------------------
@app.route('/hallo/<name>')
def hallo_name(name):
    return "Hallo, %s" %name
#---------------------------------------
@app.route('/catalog/<int:item_id>')
def catalog_item(item_id):
    return "Numer in Catalog, %d" %item_id

@app.route('/versions/<float:version>')
def versions(version):
    return "Numer Versions, %f" %version

@app.route('/path1/')
def path1():
    return "Das Route 1"

@app.route('/path2')
def path2():
    return "Das Route 2"
@app.route('/url_for-test')
def url_for_test():
    return url_for('main_page')

#http://127.0.0.1:8080/login.html
#@app.route('/login.html')
#def send_login():
#    return send_file('login.html')
#------------------------------------------------------
#url_for('static', filename = 'static.html')

#@app.route('/login', methods = ['GET','POST'])
#def login():
#    if request.method == 'POST':
#        user = request.form['name']
#        return "Request vis POST, send name  %s" % user
#    else:
#        user = request.args.get('name')
#        return "request vis GET, send name  %s" % user
#------------------------------------------------------
#redirect(location,statuscode, response)
@app.route('/redirect-to-login-page')
def redirected():
    return redirect(url_for('send_login'))

@app.route('/aborted-page')
def aborted_page():
    abort(401)
    this_is_never_exec_func()

#------------------------------------------------------
#if __name__ == "__main__":
#    #----------получение списка страниц
#    with app.test_request_context():
#        print(url_for('main_page'))
#        print(url_for('path1'))
#        print(url_for('path2'))

    #app.run(port=5225)