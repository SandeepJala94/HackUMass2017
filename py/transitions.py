
import json


def transition(pos):
    with open('../txt/pos-transitions.txt') as data_file:
        data = json.load(data_file)
        return data[pos]


# print(transition("CC"))
