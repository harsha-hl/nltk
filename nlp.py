import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Place burette above beaker with titrant")
print([(X.text, X.label_) for X in doc.ents])