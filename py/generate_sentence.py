import json
from random import random

#retrieved from manlio on stackoverflow (running low on time)
def select(container, weights):
    total_weight = float(sum(weights))
    rel_weight = [w / total_weight for w in weights]
    # Probability for each element
    probs = [sum(rel_weight[:i + 1]) for i in range(len(rel_weight))]
    for (i, element) in enumerate(container):
        if random() <= probs[i]:
            break
    return element

def make_sentences(pos_seq):
    word_corpus={}
    with open('../txt/trump-pos-corpus.json','r') as f:
        word_corpus=json.load(f)
    sentence = ''
    for pos in pos_seq:
        words = []
        weights=[]
        for key in word_corpus[pos].keys():
            words.append(key)
            weights.append(word_corpus[pos][key])
        sentence = sentence+' '+select(words, weights)
    return sentence



print(make_sentences(["NNP","CC"]))
