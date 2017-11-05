
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
        data = json.load(data_file)
        max_seq = 20
        pos_seq = [pos]

        while max_seq:
            weights = data[pos].values()
            containers = data[pos].keys()
            next_pos = select(containers,weights)
            if(next_pos=='.'):
                break
            pos_seq.append(next_pos)
        pos_seq.append('.')

        return pos_seq











