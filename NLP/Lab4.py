import spacy
from nltk.stem import PorterStemmer
nlp = spacy.load("en_core_web_sm")

stemmer=PorterStemmer()
sentence = "Spacy is a powerful NLP library in Python."

#Stemming
words = sentence.split()
print("Stemming: ")
for word in words:
    print(word,"->",stemmer.stem(word))

#Lemitization
doc = nlp(sentence)
print("\nLemitization: ")
for token in doc:
    print(token.text,"->",token.lemma_)