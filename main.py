from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
@app.get("/home")
def home():
    return render_template("home.html")


@app.get("/view")
def view():
    return render_template("view.html")


@app.get("/add")
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
