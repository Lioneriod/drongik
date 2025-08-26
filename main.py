from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route('/')

def index():
  first_name = "Lio"
  return render_template("index.html", first_name=first_name)

@app.route("/profile/<name>")

def user(name):
  return render_template("profile.html", profile_name=name)
