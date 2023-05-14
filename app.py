from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "" 
    age = "" 

    return render_template('index.html' , name = name , age = age)


if __name__  ==  '__main__':
    app.run(debug=True)
