from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
   # return "Hello, world!"
    return render_template('home.html')

app.run(port=4996) # GET http://127.0.0.1:4996/users