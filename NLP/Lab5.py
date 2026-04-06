import spacy
nlp = spacy.load("en_core_web_sm")

text = """Natural Language Processing (NLP) is a field of artificial intelligence 
that enables computers to understand and process human language. It combines 
computational linguistics with machine learning, deep learning, and statistical modeling. 
NLP is used in various applications such as chatbots, sentiment analysis, and language translation."""

doc = nlp(text)
print("Named Entities: ")
for ent in doc.ents:
    print(ent.text,"->",ent.label_)