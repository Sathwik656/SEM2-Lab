import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = """
Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a valuable way. NLP combines computational linguistics with machine learning, deep learning, statistical modeling, and more. It has various applications including chatbots, sentiment analysis, language translation, and information retrieval.
"""

words = word_tokenize(text)
stop_words = set(stopwords.words('english'))

word_freq = {}
for word in words:
    word = word.lower()
    if word not in stop_words and word.isalpha():
        if word in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

print("Word Frequencies: ")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")