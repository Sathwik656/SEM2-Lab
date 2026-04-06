import spacy
from nltk.corpus import wordnet

nlp = spacy.load("en_core_web_sm")
sentence = "The dog chased the cat up the tree."
doc = nlp(sentence)

nouns = [token.text for token in doc if token.pos_ == "NOUN"]
print("Nouns in the sentence: ", nouns)

print("\nHypernims: ")
for noun in nouns:
    synsets = wordnet.synsets(noun)
    if synsets:
        hypernyms = synsets[0].hypernyms()
        if hypernyms:
            print(noun, "->", hypernyms[0].lemma_names())