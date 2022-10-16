from flask import Flask, render_template, session, redirect, request, url_for, g
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token
from user import User
from database import Database

app = Flask(__name__)
app.secret_key = 'flashlantern'

Database.initialise(host='localhost', database='learning1', user='postgres', password='flashlantern')

@app.before_request
def load_user():
    if 'screen_name' in session:
        g.user = User.load_from_db_by_screen_name(session['screen_name'])

@app.route('/')
def homepage():
   # return "Hello, world!"
    return render_template('home.html')

@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    session['request_token'] = request_token

    #return redirect('http://example.com')
    return redirect(get_oauth_verifier_url(request_token))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))

@app.route('/auth/twitter') # http://127.0.0.1:4995/auth/twitter?oauth_verifier=1234567
def twitter_auth():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)

    user = User.load_from_db_by_screen_name(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], id)
        user.save_to_db()

    session['screen_name'] = user.screen_name

    return redirect(url_for('profile'))
    #return redirect('http://127.0.0.1:4995/profile')


@app.route('/profile')
def profile():
    return render_template('profile.html',user = g.user)
   # return render_template('profile.html',user = User.load_from_db_by_screen_name(session['screen_name']))


app.run(port=4995, debug=True)





    # GET http://127.0.0.1:4996/users
#http://127.0.0.1:4995/auth/twitter