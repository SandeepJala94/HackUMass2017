import csv
from collections import defaultdict
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
import json
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


Transition_response = defaultdict(str)
index= 0

with open('../csv/dialougues.csv','r',encoding='utf-16LE') as dialougues:
    reader = csv.reader(dialougues)
    for row in reader:
        trump_response = word_tokenize(row[6])
        trump_tags = pos_tag(trump_response)
        if (index == 0):
            index +=1
        trump_transitions = []
        for i in range(1,len(trump_tags)):
            transition = (trump_tags[i-1][1],trump_tags[i][1])
            trump_transitions.append(transition)

        other_transitions = []
        for i in range(0,6):
            other_tags = pos_tag(row[i])
            for x in range(1,len(other_tags)):
                transition = (other_tags[x-1][1],other_tags[x][1])
                other_transitions.append(transition)

        for transition in other_transitions:
            Transition_response[str(transition)]=defaultdict(str)
            for trump_transition in trump_transitions:
                try:
                    Transition_response[str(transition)][str(trump_transition)]+=1
                except Exception:
                    Transition_response[str(transition)][str(trump_transition)]=1

with open("../json/trump_response.json",'w') as f:
    json.dump(Transition_response,f)
