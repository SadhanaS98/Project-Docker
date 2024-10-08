from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to DevOps World!"

#@app.route('/')
#def hello():
#    return "Hello Devops World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
