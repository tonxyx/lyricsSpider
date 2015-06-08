import networkx as nx, sys
from nltk.tokenize import RegexpTokenizer

f=open('../rihanna.txt','rU')
raw=f.read()
raw = raw.lower()
f.close()

sentences = raw.split('\n\n')

G=nx.DiGraph()

for sentence in sentences:
    #use tokenizer to match and clean words
    tokenizer = RegexpTokenizer(r'[A-Za-z]\w+')
    tokens = tokenizer.tokenize(sentence)
    lastWord = ""
    for token in tokens:
        if (lastWord != ""):
            G.add_edge(lastWord, token)
        lastWord = token

print "\nin degree"
print G.in_degree()

print "\nout degree"
print G.out_degree()

print "\nsum of degree"
degrees = G.degree()
sum_of_edges = sum(degrees.values())
print sum_of_edges

print "\navg degree connectivity"
print nx.assortativity.connectivity.average_degree_connectivity(G)

print "\navg neighbor degree"
print nx.assortativity.average_neighbor_degree(G)

print "\navg shortest path length"
print nx.average_shortest_path_length(G)
