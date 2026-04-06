import spacy

nlp=spacy.load("en_core_web_sm")
p = """Natural Language Processing is a branch of AI.
it helps computers understand human language.
NLP is widely used in chatbots and translation systems."""

doc = nlp(p)

print("Tokenized sentence")
sentence_count = 0
for sent in doc.sents:
    print(sent.text)
    sentence_count += 1

print("\nWord tokenization")
word_count = 0
for token in doc:
    if not token.is_punct and not token.is_space:
        print(token.text)
        word_count += 1

print(f"\nTotal sentences: {sentence_count}")
print(f"Total words: {word_count}")