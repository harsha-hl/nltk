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

def getObjects(line):
    #print(word_tokenize(text))
    line = re.sub(r"[^a-zA-Z0-9]", " ", line.lower())
    words = line.split()
    #print("\n\nAfter tokenizing and converting all text to lowercase-\n ")
    #print(words)


    #print(stopwords.words("english"))
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in words if not w.lower() in stop_words]
    #print("\n\nAfter removing stop-words-\n")
    #print(filtered_sentence)

    #print("\n\nExtracting root word-\n")
    """stemmed = [PorterStemmer().stem(w) for w in words]
    print(stemmed)"""
    lemmed = [WordNetLemmatizer().lemmatize(w) for w in filtered_sentence]
    #print(lemmed)

    print("\n\nPOS tagged-\n")
    tagged = pos_tag(words)   #should have been lemmed not words
    for i in tagged:
        if i[0] in lemmed:
            print(i)

        
    position_words = ['under', 'over', 'above', 'below', 'near', 'towards']
    apparatus = ["beaker", "burette", "pipette", "bunsenburner", "burner", "roundbottomflask", "conicalflask", "tripodstand", "wiregauze","testtube"]
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
            if i[0] in apparatus:
                objects.append(i[0])
                if temp=="" and verb_temp!="" :
                    verbs[i[0]]=verb_temp;
                elif temp=="" and position_temp!="":
                    position[i[0]]=position_temp
                temp=i[0]
                count+=1
        elif i[1]=='IN':
            if i[0] in position_words:
                if i[0] == 'under' or i[0]=='below':
                    if temp!="":
                        position[temp] = "down"
                    else:
                        position_temp="down"
                elif i[0]=='above' or i[0]=='over':
                    if temp!="":
                        position[temp]="up"
                    else:
                        position_temp="up"
            else:
                if temp!= "":
                    position[temp]=i[0]
                else:
                    position_temp=i[0]
        elif i[1][0]=='V':
            if temp!="":
                verbs[temp]=i[0]
            else:
                verb_temp =i[0];
    
    x=[]

    for i in range(count):
        print("\nFor ",i,"th object")
        try:
            name=objects[i]
            print("Object is:" ,objects[i])
            fill=0
            src="abc"
            colour ="default"
            pos= position[objects[i]]
            print("Position is:",pos)
            verb = verbs[objects[i]]
            
            
        except:
           pass

        x.append({"name":name, "fill":fill,"src":src, "colour":colour,"verb":verb,"position":pos})
        pos="default";verb="default"

    return x
        

    

def main():         
    text = "Place stearic acid in a testtube boiling over a bunsen burner. "
    #print("\nBefore processing-\n")
    #print(text)
    sentence = sent_tokenize(text)
    print(sent_tokenize(text))

    for i in sentence:
        x=getObjects(i)
        print("Final output-\n",x)

main()