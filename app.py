# FLASK_APP=app.py FLASK_ENV=development flask run
import text_preprocessing 
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import json

app = Flask(__name__)  

@app.route("/")
def home():
  return render_template("h.html")  


@app.route("/experiment")
def experiment():
  objects = []    # a Python object (dict):
  new=[]
  check_box=[] 
 # para = '''Pour dilute HCl from a beaker into a test tube containing salt solution.
  #  No white precipitate formed in test tube indicating absence of Pb2+. 
 #   Pour H2S from beaker to test tube. 
  #  Black precipitate is formed in test tube indicating presence of Cu2+ or Pb2+.
  #  Pour HNO3 from conicalflask to test tube.
  #  Solution in test tube turns green.
  #  Divide the solution into two and pour NH4OH solution from beaker to test tube containing one part. 
  #  Solution in test tube turns blue confirming presence of Cu2+.
  #  Pour K4[Fe(CN)6] solution from conicalflask to test tube containing second part. 
  #  Chocolate brown precipitate of Copper ferrocyanide is formed in test tube confirming the presence of Cu2+ ions.
  #  '''



  para = ''' Add a few drops of dilute H2SO4 (sulfuric acid) from conical flask to a small quantity of the salt in a test tube.
Light brown gas with a pungent smell is evolved from the test tube.
The anion maybe Nitrate.
Add Iron(II) Sulphate from beaker to the test tube containing salt solution.
Add acid (H2SO4) from the container to the corners of the test tube. 
A Brown ring is formed at the junction of the acid and the solution in the test tube.
Nitrate is confirmed. 

Add a few drops of Hcl from container to the test tube containing salt solution.
No change observed.
To the above solution in test tube, pass H2S gas.
No changes observed.
Add solid NH4Cl to the test tube containing salt solution and then add excess NH4OH from conical flask.
Add ammonium carbonate, ammonium chloride, and ammonium hydroxide to the original solution in the test tube.
Black precipitate is obtained in the test tube.
Cation maybe Barium, Strontium or Calcium.
Add K2Cr2O4 from conical flask to test tube containing salt solution. A yellow precipitate is formed.
CAtion maybe Ba2+
Make a paste of the salt by mixing it in a petri dish. Add a few drops of concentrated hydrochloric acid. Now skim off some of the paste with a glass rod and expose it above a Bunsen Burner’s flame.
Green coloured flame confirms Ba2+ as cation.

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
    
  #return render_template("index.html", objs = objects)
  return render_template("index.html", objs = new, para=para,abc=check_box, instruments = apparatus)  
      
  
  
    
    

  
  
  
  