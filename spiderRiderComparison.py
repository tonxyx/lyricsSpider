import nltk, re, json
from nltk.tokenize import RegexpTokenizer

# get 10 most used words from one artist
def getMostUsed (artistName, artistFile):
    #open file and read, put all word to lowercase so we have no duplicates
    f=open(artistFile,'rU')
    raw=f.read()
    raw = raw.lower()
    f.close()

    #add unnecesarry words to remove list and join them for regex
    removeList = ["the", "and", "it", "in", "is", "don", "re", "ll", "ve", "chorus", "na", "of", "be", "oh", "to", "so"]
    remove = '|'.join(removeList)

    #compile regex and run it on raw text
    filterRegex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE);
    raw = filterRegex.sub("", raw);

    #use tokenizer to match and clean words (at least 4 letters for better visualization)
    tokenizer = RegexpTokenizer(r'[A-Za-z]{4,}\w+');
    tokens = tokenizer.tokenize(raw);

    #use frequency distance on tokens and get 10 most used
    fdist1 = nltk.FreqDist(tokens);
    words = fdist1.most_common(10);

    word_array = []
    for (word, freq) in words:
        word_array.append({'name' : word, 'size' : freq})

    return {'name' : artistName, 'size' : len(set(tokens)), 'children' : word_array}

comparisonArray = {
    'name' : 'Artists',
    'children' : [
        getMostUsed('Bob Marley', 'bob_marley.txt'),
        getMostUsed('Eminem', 'eminem.txt'),
        getMostUsed('Metallica', 'metallica.txt'),
        getMostUsed('Queen', 'queen.txt'),
        getMostUsed('Rihanna', 'rihanna.txt')
    ]
}

file = open('mostUsedComparison/data.tsv','w')

file.write(json.dumps(comparisonArray))

file.close()
