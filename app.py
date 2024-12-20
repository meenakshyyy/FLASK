from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template("Hello.html")

@app.route("/",methods=["POST"])
def my_form_post():
    text=request.form["text"]
    return"<h1> {} </h1>".format(text)

if __name__=="__main__":
    app.run(debug=True)