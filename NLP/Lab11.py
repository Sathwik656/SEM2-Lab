from nltk import CFG
from nltk.parse import ShiftReduceParser

grammar = CFG.fromstring("""
S -> NP VP  
NP -> Det N
VP -> V NP
Det -> "The" | "the"
N -> "boy" | "ball"
V -> "kicked"
""")

sentence = "The boy kicked the ball".split()

parser = ShiftReduceParser(grammar)

for tree in parser.parse(sentence):
    print("Hello")
    print(tree)
    tree.pretty_print()