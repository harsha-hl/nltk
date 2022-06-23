from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import json

app = Flask(__name__)  

@app.route("/")
def hello_world():
    objects = []    # a Python object (dict):
    obj1 = {
      "name": "burette",
      "fill": 0,
      "src": "srwrfrwe",
      "color": "nil",
      "verb": "nil",
      "action": "nil",
      "pos": "under" 
    }
    obj2 = {
      "name": "beaker",
      "fill": 1,
      "src": "sfvsd",
      "color": "blue",
      "verb": "pour",
      "action": "nil",
      "pos": "default" 
    }
    objects.append(json.dumps(obj1))
    objects.append(json.dumps(obj2))

    return render_template("index.html", objs = objects) 