# FLASK_APP=main.py FLASK_ENV=development flask run
import text_preprocessing 
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import json

app = Flask(__name__)  

@app.route("/")
def hello_world():
  objects = []    # a Python object (dict):
  new=[]
  para = '''Place stearic acid in a testtube boiling over a bunsen burner.
            Then put a testtube in the roundbottomflask. 
            Then put a beaker in burette.
            Then pouring the contents of the testtube into the conicalflask.'''
  #length = text_preprocessing.sen()    #var is the no of sentences in the paragraph
  qwe=text_preprocessing.main()   # qwe={(name:testtube,pos:up),(name:beaker,pos:down)}
  var = text_preprocessing.sen()
  print("this is var",var)
  for i in range(var):    #if return render_template is within this for loop only the objects of first sentence are displayed
    print("this is newest",qwe[i])   #qwe[i] is each sentence
    for q in qwe[i]:
        print("this is individual objects in each sent",q)
        objects.append(json.dumps(q))
    new.append(objects)
    objects=[]
  print("\n\n\neeeeeeeeeeeeee\n\n\n",new)
    
  #return render_template("index.html", objs = objects)
  return render_template("index.html", objs = new, para=para)  
      
  
  
    
    

  
  
  
  