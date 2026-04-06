from nltk.corpus import wordnet
word = "bank"
synsets = wordnet.synsets(word)
for syn in synsets[:3]:
    print("Meaning: ",syn.definition())
