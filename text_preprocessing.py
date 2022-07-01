import nltk
#nltk.download('punkt',halt_on_error=False)
#nltk.download('stopwords', halt_on_error=False)
#nltk.download('wordnet',halt_on_error=False)
#nltk.download('averaged_perceptron_tagger',halt_on_error=False)
#nltk.download('omw-1.4',halt_on_error=False)
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from nltk.probability import FreqDist
from bs4 import BeautifulSoup

global text
text = '''Pour dilute HCl from a beaker into a testtube containing salt solution. 
    No white precipitate formed indicating absence of Pb2+. Add H2S from beaker to testtube. 
    Black precipitate is formed indicating presence of Cu2+ or Pb2+.
    Pour HNO3 from conicalflask to testtube containing precipitate.
    Precipitate dissolves and solution in testtube turns bluishgreen.
    Divide the solution into two parts and add NH4OH solution from beaker to testtube containing one part. 
    Solution in testtube turns deepblue confirming presence of Cu2+.
    Add K4[Fe(CN)6] solution from conicalflask to testtube containing second part. 
    Chocolate brown precipitate of Copper ferrocyanide is formed in testtube confirming the presence of Cu2+ ions.'''

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

    objects =[]
    positionx={}
    positiony={}
    verbs={}
    count=0
    temp=""
    verb_temp=""
    positionx_temp =""
    positiony_temp =""
    verb="default";posx="400"; flag=0;posy="-600"


    for i in tagged:
        if i[1] == 'NN':
            if bs.find('obj', {'name':i[0]}) != None:
                objects.append(i[0])
                
                print("temp is",temp)
                if temp=="" and verb_temp!="" :
                    verbs[i[0]]=verb_temp
                
                if temp=="" and positiony_temp !="":
                    print("I am Here", temp)
                    positionx[i[0]]=positionx_temp
                    positiony[i[0]]=positiony_temp
                temp=i[0]
                
                count+=1
        elif i[1]=='IN':
            p=bs.find('pos',{'name':i[0]})
            print("P is:",i[0],p,temp)
            print("temp is", temp)
            if p != None:
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

        elif i[1][0]=='V':
            if temp!="":
                verbs[temp]=i[0]
            else:
                verb_temp =i[0];
        
        
    
    x=[]
    
    print("\n\n\nobj,pos,verb,count",objects)

   
    for i in range(count):
        print("\nFor ",i,"th object")
        
        name=objects[i]
        print("Object is:" ,objects[i])
        fill=0
        img=bs.find('img',{"name": objects[i]})
        src= img.get('src')
        colour ="default"
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

        x.append({"name":name, "fill":fill,"src":src, "colour":colour,"verb":verb,"positionx":posx, "positiony":posy})
        posx=""; posy=""
        verb="default"
    
        print(x)
    return x

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