# Find common linguistic patterns
# in Donald Trump Tweets

import re
from collections import defaultdict
import json

# Get the contents of the file
# Delimit by spaces and grab the last element
f = open('../txt/trump_tweets_pos.txt', 'r', encoding='utf-8')
dictionary={}
i = 0

for line in f:
    dictionary
    i+=1

    #print(i)
    # Delimit the line by space
    line_split = line.split(" ")
    # Get the word
    word = line.split(" ")[0].lower()
    # Get the pos
    PoS=line_split[1].replace("\n", "")
    # Determine if the part of speech is a key in the dictionary
    # see if the word exists in the dictionary and the word is
    # not a link or @ or #

    try:
        print()
        dictionary[PoS][word]+=1
    except Exception:
        try:
            dictionary[PoS][word]=1
        except Exception:
            dictionary[PoS]={}
            dictionary[PoS][word]=1

#for elem in dictionary:
    #print(elem)
with open('../txt/trump-pos-corpus.json', 'w') as f:
    json.dump(dictionary,f)
