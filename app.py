from flask import Flask, render_template, url_for, request, redirect
import random

app = Flask(__name__)

x = 5
namen = ["Max", "Lukas", "Sarah"]
dict_data = {"name": "Max", "age": 27}

database = []


# @app.route("/")
# def home():
#     return """
#     <h1>Hallo</h1>
#     """

@app.route("/")
def home():
    return render_template("index.html", variable=x, namen=namen, dict_data=dict_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard/<int:login_id>")
def dashboard(login_id):
    for entry in database:
        if entry.get("id") == login_id:
            print("entry found")
            return render_template("dashboard.html", result=entry)
    return render_template("404.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname= request.form.get("lname")
        name = f'{fname} {lname}'
        entry = {"id": random.randint(0, 100), "name": name}
        database.append(entry)
        print(database)
        return redirect(url_for("dashboard", login_id=entry.get("id")))
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4000, debug=True)