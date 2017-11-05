import json
from collections import Counter
import operator

#retrieved from stack overflow
def parse_tuple(string):
    try:
        s = eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return

def best_pos(seq):
    trump_pos = None
    with open("../json/pos-transitions.json") as f:
        trump_pos=json.load(f)
    dictionary = {}
    for i in seq:
        key1 = str(i[0])
        key2 = str(i[1])
        d_update = trump_pos.get(key1)
        if d_update==None:
            continue
        dictionary=dict(Counter(d_update)+Counter(dictionary))

    if "." in dictionary:
        del myDict['.']

    max_key=max(dictionary.items(), key=operator.itemgetter(1))

    return max_key[0]
