import spacy
nlp = spacy.load("en_core_web_sm")

sentence = "Spacy is a powerful NLP library in Python."
doc = nlp(sentence)

print("Pos tagging: ")
for token in doc:
    print(token.text,"->",token.pos_)

#Remove Stopwords
filwords = [token.text for token in doc if not token.is_stop and not token.is_punct]
filsent = " ".join(filwords)
print("\nFiltered sentence: ",filsent)