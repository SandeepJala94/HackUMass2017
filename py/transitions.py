
import json
from random import randint
import operator

sorted_pos_dict = dict()


from random import random


weights_list = []


def select(container, weights):
    total_weight = float(sum(weights))
    rel_weight = [w / total_weight for w in weights]

    # Probability for each element
    probs = [sum(rel_weight[:i + 1]) for i in range(len(rel_weight))]

    for (i, element) in enumerate(container):
        if random() <= probs[i]:
            break
    return element


def transition(pos):

    with open('../json/pos-transitions.json') as data_file:
        print(31)
        data = json.load(data_file)
        print(33)
        max_seq = 20
        print(35)
        pos_seq = [pos]
        print(37)
        while max_seq:
            print(39)
            weights = data[pos].values()
            containers = data[pos].keys()
            next_pos = select(containers,weights)
            pos_seq.append(next_pos)
            max_seq-=1

        return pos_seq





print(transition("."))
