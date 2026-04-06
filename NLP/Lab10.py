from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP  
NP -> Det N
VP -> V NP
Det -> "The" | "the"
N -> "boy" | "ball"
V -> "kicked"
""")

sentence = "The boy kicked the ball".split()

parser = RecursiveDescentParser(grammar)

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()