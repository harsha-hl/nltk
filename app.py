# FLASK_APP=app.py FLASK_ENV=development flask run
import text_preprocessing 
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import json

app = Flask(__name__)  

@app.route("/")
def hello_world():
  objects = []    # a Python object (dict):
  new=[]
  check_box=[] 
  para = '''Pour dilute HCl from a beaker into a test tube containing salt solution.
          No white precipitate formed indicating absence of Pb2+. 
    Pour H2S from beaker to test tube. 
    Black precipitate is formed indicating presence of Cu2+ or Pb2+.
    Pour HNO3 from conicalflask to test tube containing precipitate.
    Precipitate dissolves and solution in test tube turns bluishgreen.
    Divide the solution into two parts and pour NH4OH solution from beaker to test tube containing one part. 
    Solution in test tube turns deepblue confirming presence of Cu2+.
    Pour K4[Fe(CN)6] solution from conicalflask to test tube containing second part. 
    Chocolate brown precipitate of Copper ferrocyanide is formed in test tube confirming the presence of Cu2+ ions.
    '''

  #length = text_preprocessing.sen()    #var is the no of sentences in the paragraph
  qwe=text_preprocessing.main()   # qwe={(name:testtube,pos:up),(name:beaker,pos:down)}
  var = text_preprocessing.sen()
  apparatus = text_preprocessing.apparatus() 
  print("this is var",var)
  for i in range(var):    #if return render_template is within this for loop only the objects of first sentence are displayed
    print("this is newest",qwe[i])   #qwe[i] is each sentence
    for q in qwe[i]:
        print("this is individual objects in each sent",q)
        objects.append(json.dumps(q))
    new.append(objects)
    check_box.append(objects)
    objects=[]
  print("\n\n\neeeeeeeeeeeeee\n\n\n",new)
    
  #return render_template("index.html", objs = objects)
  return render_template("index.html", objs = new, para=para,abc=check_box, instruments = apparatus)  
      
  
  
    
    

  
  
  
  