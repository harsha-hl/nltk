from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify

app = Flask(__name__)  

@app.route("/")
def hello_world():
    return render_template("index.html") 