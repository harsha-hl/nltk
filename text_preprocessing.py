import nltk
#nltk.download('punkt',halt_on_error=False)
#nltk.download('stopwords', halt_on_error=False)
#nltk.download('wordnet',halt_on_error=False)
#nltk.download('averaged_perceptron_tagger',halt_on_error=False)
#nltk.download('omw-1.4',halt_on_error=False)
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from nltk.probability import FreqDist
from bs4 import BeautifulSoup

a = []
global text
text = '''Pour dilute HCl from a beaker into a test tube containing salt solution.
    No white precipitate formed indicating absence of Pb2+. 
    Pour H2S from beaker to test tube. 
    Black precipitate is formed indicating presence of Cu2+ or Pb2+.
    Pour HNO3 from conicalflask to test tube.
    Solution in test tube turns green.
    Divide the solution into two parts and pour NH4OH solution from beaker to test tube containing one part. 
    Solution in test tube turns blue confirming presence of Cu2+.
    Pour K4[Fe(CN)6] solution from conicalflask to test tube containing second part. 
    Chocolate brown precipitate of Copper ferrocyanide is formed in test tube confirming the presence of Cu2+ ions.
    '''

def getObjects(line):
    line = re.sub(r"[^a-zA-Z0-9]", " ", line.lower())
    words = line.split()
    
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in words if not w.lower() in stop_words]
    
    lemmed = [WordNetLemmatizer().lemmatize(w) for w in filtered_sentence]

    print("\n\nPOS tagged-\n")
    tagged = pos_tag(words)   #should have been lemmed not words
    print(tagged)
    '''for i in tagged:
        if i[0] in lemmed:
            print(i)
    '''

    with open('data.xml', 'r') as f:
        data = f.read()
    bs = BeautifulSoup(data, "xml")

    verb_count=0
    objects =[]
    positionx={}
    positiony={}
    colours={}
    verbs={}
    count=0
    temp=""
    verb_temp=""
    positionx_temp ="400"
    positiony_temp ="-600"
    colour_temp=""
    verb="default";posx=""; flag=0;posy=""
    colour="#cccccc"


    for i in tagged:

        if i[1] == 'NN':
            if bs.find('obj', {'name':i[0]}) != None:
                objects.append(i[0])
                a.append(i[0])
                print("temp is NN",temp)
                if temp=="" and verb_temp!="" :
                    verbs[i[0]]=verb_temp
                
                if temp=="" and positiony_temp !="":
                    print("I am Here", temp)
                    positionx[i[0]]=positionx_temp
                if temp=="" and colour_temp != "":
                    colours[i[0]] = colour_temp
                    positiony[i[0]]=positiony_temp
                temp=i[0]
                print("temp is NN2",temp)
                count+=1
        elif i[1]=='IN':
            p=bs.find('pos',{'name':i[0]})
            print("P is:",i[0],p,temp)
            
            if p != None:
                print("temp is IN", temp)
                if temp!="":
                    print("here 1")
                    positionx[temp]= p.get('x')
                    positiony[temp]= p.get('y')
                    print("position type-", p.get('name'))
                    print("Y is:",positiony[temp], temp)

            
                else:
                    print("here 2")
                    positionx_temp=p.get('x')
                    positiony_temp=p.get('y')
                    print(positiony_temp,positionx_temp)

        elif i[1][0]=='V' or i[1]=='NNS':
            if temp!="" and verb_count==0:
                verbs[temp]=i[0]
            elif verb_count==0:
                verb_temp =i[0];
                print("Verb_temp", verb_temp)
            verb_count+=1

        elif i[1]=="JJ":
            cc = bs.find('colour', {'name':i[0]})
            if cc != None:
                if temp!="":
                    colours[temp]=cc.get('hex')
                else:
                    colour_temp= cc.get('hex')
    x=[]
    
    print("\n\n\nobj,pos,verb,count",objects,positionx,positiony,verbs)

   
    for i in range(count):
        print("\nFor ",i,"th object")
        
        name=objects[i]
        print("Object is:" ,objects[i])
        fill=0
        img=bs.find('img',{"name": objects[i]})
        src= img.get('src')
        try:
            colour = colours[objects[i]]
        except:
            pass

        try:
            posx= positionx[objects[i]]
            posy= positiony[objects[i]]
            print("Position is:",posx)
        except:
           pass
        try:
            verb = verbs[objects[i]]            
            
        except:
           pass
        if posx == "" or posy=="":
            posx= "400"
            posy= "-600"
        if verb=='pour':
            src="static/"+name+"_pour.png"
            posx="420"
            posy="-500"
        if name=='precipitate':
            posx="390"
            posy="-691"
        x.append({"name":name, "fill":fill,"src":src, "colour":colour,"verb":verb,"positionx":posx, "positiony":posy})
        posx=""; posy=""
        verb="default"
    
        print(x)
    return x


def apparatus():
    print(a)
    b=[]
    for i in a:
        if i not in b:
            b.append(i)

    return b


def sen():
    abc = sent_tokenize(text)
    sent_len=len(abc)
    return(sent_len) 


def main():         
    sentence = sent_tokenize(text)
    print(sent_tokenize(text))
    obj=[]
    for i in sentence:
        x=getObjects(i)
        obj.append(x)
    print("Final output-\n",obj)
    return obj
        
main()