
import json


def transition(pos):
    data = None
    with open('../txt/pos-transitions.json') as data_file:
        print(data_file)
        data = json.load(data_file)
    print(data["CC"])










print(transition("CC"))
