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
global text, text2, text3
f = open("static/text/titration.txt", "r")
text = f.read()

f = open("static/text/basic_radical.txt", "r")
text2= f.read()

f= open("static/text/salt_analysis.txt", "r")
text3 = f.read()

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
    positionx_temp ="500"
    positiony_temp ="-600"
    colour_temp=""
    verb="default";posx=""; flag=0;posy=""
    colour="#cccccc"
    check_verb = ["add", "pour"]


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
                    positiony[i[0]]=positiony_temp
                if temp=="" and colour_temp != "":
                    print("Temp is", temp)
                    print("Colour temp  is ", colour_temp)
                    colours[i[0]] = colour_temp
                    colour_temp=""                    
                temp=i[0]
                print("temp is NN2",temp)
                count+=1
        if i[1]=='IN':
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

        if i[1][0]=='V' or i[1]=='NNS' or i[1] == 'JJ':
            if temp!="" and verb_count==0:
                verbs[temp]=i[0]
            elif verb_count==0:
                verb_temp =i[0];
                print("Verb_temp", verb_temp)
            verb_count+=1

        if i[1]=="JJ" or i[1]=='IN':
            print(i[0],"This is colourrrrrrrrrr")
            cc = bs.find('colour', {'name':i[0]})

            if cc != None:
                if temp!="":
                    colours[temp]=cc.get('hex')
                else:
                    colour_temp= cc.get('hex')
    x=[]
    
    print("\n\n\nobj,pos,verb,colours",objects,positionx,positiony,verbs,colours)

   
    for i in range(count):
        print("\nFor ",i,"th object")
        
        name=objects[i]
        print("Object is:" ,objects[i])
        fill=0
        img=bs.find('img',{"name": objects[i]})
        src= img.get('src')
        try:
            colour = colours[objects[i]]
            print("COLOURRRR ", colour)
        except:
            colour="#cccccc"

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
            posx= "500"
            posy= "-600"
        if verb in check_verb:
            src="static/"+name+"_pour.png"
            posx="310"        
            posy="-425"       
        if name=='precipitate':
            posx="507"
            posy="-593"
        if name == 'ring':
            posx="470"
        if name == "burner" and colour=="#cccccc":
            colour = "#e25822"
        x.append({"name":name, "fill":fill,"src":src, "colour":colour,"verb":verb,"positionx":posx, "positiony":posy})
        posx=""; posy=""
        verb="default"
        if i==1:
            temp_array = x[1]
            x[1]= x[0]
            x[0]=temp_array
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
    #abc = sent_tokenize(text2)
    abc = sent_tokenize(text3)
    sent_len=len(abc)
    return(sent_len) 


def main():         
    #sentence = sent_tokenize(text)
    sentence = sent_tokenize(text3)
    #print(sent_tokenize(text))
    print(sent_tokenize(text3))
    obj=[]
    for i in sentence:
        x=getObjects(i)
        obj.append(x)
    print("Final output-\n",obj)
    return obj
        
main()



def sen1():
    #abc = sent_tokenize(text2)
    abc = sent_tokenize(text2)
    sent_len=len(abc)
    return(sent_len) 


def main1():         
    #sentence = sent_tokenize(text)
    sentence = sent_tokenize(text2)
    #print(sent_tokenize(text))
    print(sent_tokenize(text2))
    obj=[]
    for i in sentence:
        x=getObjects(i)
        obj.append(x)
    print("Final output-\n",obj)
    return obj
        
main()



def sen2():
    #abc = sent_tokenize(text2)
    abc = sent_tokenize(text)
    sent_len=len(abc)
    return(sent_len) 


def main2():         
    #sentence = sent_tokenize(text)
    sentence = sent_tokenize(text)
    #print(sent_tokenize(text))
    print(sent_tokenize(text))
    obj=[]
    for i in sentence:
        x=getObjects(i)
        obj.append(x)
    print("Final output-\n",obj)
    return obj
        
main()