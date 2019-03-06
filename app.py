from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def intex():
    return render_template('index.html')
    
@app.route("/home")
def home():
    return "Welcome to Our Home Page"

@app.route("/contacts")
def contact():
    return "These are your Contacts"

@app.route("/about")
def about():
    return "Know more about us"

if (__name__=="__main__"):
    app.run(debug=True)