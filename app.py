#import text_preprocessing 
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import json

app = Flask(__name__)  

@app.route("/")
def hello_world():
    #var = text_preprocessing.main()
    #print(var)
    #for i in var:
     # obj1 = i
      

  #  new_x= main.x
    #print(new_x)
    objects = []    # a Python object (dict):
    
   # dict = [["beaker", "static/beaker.png"],["conical flask", "static/conical.png"],["bunsen burner", "static/bunsen_burner.png"],["burette", "static/burette.png"],["funnel", "static/funnel.png"],["measuring cylinder", "static/measuring_cylinder.png"],["paper", "static/paper.png"],["round bottom flask", "static/round_bottom_flask.png"],["test tube", "static/test_tube.png"],["tongs", "static/tongs.png"]]
   # var="conical"

   # objects.append(json.dumps(new_x))

    #for i in range(len(dict)):
     # if(dict[i][0] == var):
      #  print(dict[i][1])
       # setattr(self.obj1,'image',dict[i][1])
    
    
    obj1 = {
      "name": "testtube",
      "fill": 0,
      "src": "static/test_tube.png",
      "color": "default",
      "verb": "default",
      "pos": "up"
          }
    obj2 = {
      "name": "burner",
      "fill": 0,
      "src": "static/bunsen_burner.png",
      "color": "default",
      "verb": "default",
      "pos": "default"
    }
    obj3 = {
      "name": "round bottom flask",
      "fill": 0,
      "src": "static/round_bottom_flask.png",
      "color": "default",
      "verb": "default",
      "pos": "default"
    }
    obj4 = {
      "name": "thermometer",
      "fill": 0,
      "src": "static/thermometer1.png",
      "color": "default",
      "verb": "default",
      "pos": "inside"
    }
    obj5 = {
      "name": "conical flask",
      "fill": 0,
      "src": "static/conical.png",
      "color": "default",
      "verb": "pour",
      "pos": "default"
    }
    obj6 = {
      "name": "beaker",
      "fill": 0,
      "src": "static/beaker.png",
      "color": "default",
      "verb": "default",
      "pos": "default"
    }
    objects.append(json.dumps(obj1))
    objects.append(json.dumps(obj2))
    objects.append(json.dumps(obj3))
    objects.append(json.dumps(obj4))
    objects.append(json.dumps(obj5))
    objects.append(json.dumps(obj6))
   # hello_world()
   # var = text_preprocessing.main()
   # print("var is",var)
    return render_template("index.html", objs = objects) 
  