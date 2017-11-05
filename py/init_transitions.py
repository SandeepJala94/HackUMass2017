# Make a markov model based on the bigram_counts.txt file
import json

markov = dict()
markov["CC"] = []
markov["CD"] = []
markov["DT"] = []
markov["EX"] = []
markov["FW"] = []
markov["IN"] = []
markov["JJ"] = []
markov["JJR"] = []
markov["JJS"] = []
markov["LS"] = []
markov["MD"] = []
markov["NN"] = []
markov["NNS"] = []
markov["NNP"] = []
markov["NNPS"] = []
markov["PDT"] = []
markov["POS"] = []
markov["PRP"] = []
markov["PRP$"] = []
markov["RB"] = []
markov["RBR"] = []
markov["RBS"] = []
markov["RP"] = []
markov["SYM"] = []
markov["TO"] = []
markov["VB"] = []
markov["VBD"] = []
markov["VBG"] = []
markov["VBN"] = []
markov["VBP"] = []
markov["VBZ"] = []
markov["WDT"] = []
markov["WP"] = []
markov["WP$"] = []
markov["WRB"] = []

f = open('../txt/bigram_counts.txt', 'r')

isfound = False
lines = []
for l in f:
    isfound = False
    if l is not "\n":
        line = l
        split = line.split(" ")
        print("1->", split)
        pos_trans, freq = split[0], int(split[1].replace("\n", ""))
        split = pos_trans.split(",")
        print("2->", split)
        first_pos, second_pos = split[0], split[1].replace(":", "")
        for j, markov_element in enumerate(markov[first_pos]):
            print(second_pos, ",", markov_element[0])
            print(markov_element)
            print(second_pos)
            if markov_element[0] == second_pos:
                markov[first_pos][j] = (second_pos, markov[first_pos][j][1] + freq)
                isfound = True
                break
            else:
                isfound = False

        if not isfound:
            markov[first_pos].append((second_pos, freq))
            print('nva--------------------------------------')
            isfound = True

        for j, markov_element in enumerate(markov[second_pos]):
            if markov[second_pos][j][0] == first_pos:
                markov[second_pos][j] = (first_pos, markov_element[1] + freq)
                isfound = True
                break
            else:
                isfound = False

        if not isfound:
            markov[second_pos].append((first_pos, freq))
            isfound = True

with open('../txt/pos-transitions.txt', 'w') as outfile:
    json.dump(markov, outfile)

print(markov)


