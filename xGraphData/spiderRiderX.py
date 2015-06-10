import nltk, re, json
from nltk.tokenize import RegexpTokenizer

f=open('xGraphData.json','rU')
raw=f.read()
f.close()

ar = json.loads(raw)

cArr = {
    'name': 'Artist statistics',
    'children': []
}

for val in ar:
    for v, data in val.items():
        helpArr = []
        sizeM = 1
        for d, a in data.items():
            if (d == 'degreeAvg'):
                sizeM = a
            helpArr.append({'name': d, 'size': a})
    cArr['children'].append({'name': v, 'size': sizeM , 'children': helpArr},)

f = open('../mostUsedGroup/xGraphDataComp.tsv', 'w')
f.write(json.dumps(cArr))
f.close()
