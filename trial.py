import nltk
#nltk.download('punkt',halt_on_error=False)
#nltk.download('stopwords', halt_on_error=False)
#nltk.download('wordnet',halt_on_error=False)
#nltk.download('averaged_perceptron_tagger',halt_on_error=False)
#from nltk.tokenize import sent_tokenize, word_tokenize
import re
from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from nltk.probability import FreqDist


text = "A known volume of the unknown concentration solution should be placed in a beaker under the burette. "

print("\nBefore processing-\n")
print(text)

#print(sent_tokenize(text))
#print(word_tokenize(text))
text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
words = text.split()
print("\n\nAfter tokenizing and converting all text to lowercase-\n ")
print(words)


#print(stopwords.words("english"))
stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in words if not w.lower() in stop_words]
print("\n\nAfter removing stop-words-\n")
print(filtered_sentence)

print("\n\nExtracting root word-\n")
"""stemmed = [PorterStemmer().stem(w) for w in words]
print(stemmed)"""
lemmed = [WordNetLemmatizer().lemmatize(w) for w in filtered_sentence]
print(lemmed)

print("\n\nPOS tagged-\n")
tagged = pos_tag(words)   #should have been lemmed not words
for i in tagged:
    if i[0] in lemmed:
        print(i)


print("\n\nCreating a dictionary with most commonly used words\n")
fdist = FreqDist(lemmed)
print(fdist)
for key in sorted(fdist):
    print(key,fdist[key])
    