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
text = "Place stearic acid in a testtube boiling over a bunsen burner. Then put a testtube in the roundbottomflask. Then put a pipette in burette. Then pour the contents of the wiregauze into the tripodstand."

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
    position={}
    verbs={}
    count=0
    temp=""
    verb_temp=""
    position_temp =""
    verb="default";pos="default"; flag=0


    for i in tagged:
        if i[1] == 'NN':
            if bs.find('obj', {'name':i[0]}) != None:
                objects.append(i[0])
                if temp=="" and verb_temp!="" :
                    verbs[i[0]]=verb_temp
                elif temp=="" and position_temp!="":
                    position[i[0]]=position_temp
                temp=i[0]
                count+=1
        elif i[1]=='IN':
            p=bs.find('pos',{'name':i[0]})
            print("P is:",i[0],p)
            if p != None:
                if temp!="":
                    position[temp]= p.get('type')
                    print("type-", p.get('type'))
            
                else:
                    position_temp=p.get('type')
        elif i[1][0]=='V':
            if temp!="":
                verbs[temp]=i[0]
            else:
                verb_temp =i[0];
    
    x=[]
    print("\n\n\nobj,pos,verb,count",verbs)

   
    for i in range(count):
        print("\nFor ",i,"th object")
        try:
            name=objects[i]
            print("Object is:" ,objects[i])
            fill=0
            img=bs.find('img',{"name": objects[i]})
            src= img.get('src')
            colour ="default"
            pos= position[objects[i]]
            print("Position is:",pos)
            verb = verbs[objects[i]]            
            
        except:
           pass

        x.append({"name":name, "fill":fill,"src":src, "colour":colour,"verb":verb,"position":pos})
        pos="default";verb="default"
        
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