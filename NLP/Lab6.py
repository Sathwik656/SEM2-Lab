from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> "The" | "an"
N -> "boy" | "Apple"
V -> "eats"
""")

parser = ChartParser(grammar)

sentence = "The boy eats an Apple"
words = sentence.split()

for tree in parser.parse(words):
    print(tree)
    tree.pretty_print()