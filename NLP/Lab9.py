import spacy
from nltk.util import ngrams
text = "Natural Language Processing is a fascinating field of Artificial Intelligence."
tokens = text.split()

#Unigrams
unigrams = list(ngrams(tokens, 1))
print("Unigrams: ",unigrams)

#Bigrams
bigrams = list(ngrams(tokens, 2))
print("Bigrams: ",bigrams)

#Trigrams
trigrams = list(ngrams(tokens, 3))
print("Trigrams: ",trigrams)