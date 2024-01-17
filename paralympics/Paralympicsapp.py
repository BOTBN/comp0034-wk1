from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, welcome to my Palalympics app!"

app.route('/user/<name>')
def personalised_home(  name ):
    return f' Hello {name}! Welcome to my Paralympics app!'

if __name__== '__main__':
    app.run(debug=True)

