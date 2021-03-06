import networkx as nx, sys, json
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

data = {}
data['Rihanna'] = {}

print "\nin degree generated"
inDegree = G.in_degree()
sum = 0
count = 0
for degree, percent in inDegree.items():
    sum += percent
    count += 1

data['Rihanna']['inDegreeAvg'] = sum/count

print "\nout degree generated"
outDegree = G.out_degree()
sum = 0
count = 0
for degree, percent in outDegree.items():
    sum += percent
    count += 1

data['Rihanna']['outDegreeAvg'] = sum/count

print "\navg of degree generated"
degrees = G.degree()
sum = 0
count = 0
for degree, percent in degrees.items():
    sum += percent
    count += 1

data['Rihanna']['degreeAvg'] = sum/count

print "\navg degree connectivity generated"
avgDegreeConn = nx.assortativity.connectivity.average_degree_connectivity(G)
sum = 0
count = 0
for degree, percent in avgDegreeConn.items():
    sum += percent
    count += 1

data['Rihanna']['avgDegreeConn'] = sum/count

print "\navg neighbor degree generated"
avgNeighborDeg = nx.assortativity.average_neighbor_degree(G)
sum = 0
count = 0
for degree, percent in avgNeighborDeg.items():
    sum += percent
    count += 1

data['Rihanna']['avgNeighborDeg'] = sum/count

print "\navg shortest path length generated"
data['Rihanna']['avgShortPathLen'] = nx.average_shortest_path_length(G)

f = open('xGraphData.json', 'a')
f.write(', ')
json.dump(data, f)
f.close()

print data
