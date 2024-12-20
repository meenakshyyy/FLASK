from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template("iris.html")

@app.route("/result", methods=["POST"])
def my_result_page():
    sl=request.form["sl"]
    sw=request.form["sw"]
    pl=request.form["pl"]
    pw=request.form["pw"]
    
    return render_template("result.html",sl=sl,sw=sw,pl=pl,pw=pw)

if __name__=="__main__":
    app.run(debug=True)