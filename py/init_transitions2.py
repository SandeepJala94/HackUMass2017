# Make a markov model based on the bigram_counts.txt file
import json

markov = dict()
markov["CC"] = dict()
markov["CD"] = dict()
markov["DT"] = dict()
markov["EX"] = dict()
markov["FW"] = dict()
markov["IN"] = dict()
markov["JJ"] = dict()
markov["JJR"] = dict()
markov["JJS"] = dict()
markov["LS"] = dict()
markov["MD"] = dict()
markov["NN"] = dict()
markov["NNS"] = dict()
markov["NNP"] = dict()
markov["NNPS"] = dict()
markov["PDT"] = dict()
markov["POS"] = dict()
markov["PRP"] = dict()
markov["PRP$"] = dict()
markov["RB"] = dict()
markov["RBR"] = dict()
markov["RBS"] = dict()
markov["RP"] = dict()
markov["SYM"] = dict()
markov["TO"] = dict()
markov["VB"] = dict()
markov["VBD"] = dict()
markov["VBG"] = dict()
markov["VBN"] = dict()
markov["VBP"] = dict()
markov["VBZ"] = dict()
markov["WDT"] = dict()
markov["WP"] = dict()
markov["WP$"] = dict()
markov["WRB"] = dict()

f = open('../txt/bigram_counts.txt', 'r')

for l in f:
    line = l
    if l is not "\n":
        split = line.split(" ")
        pos_trans, freq = split[0], int(split[1].replace("\n", ""))
        split = pos_trans.split(",")
        first_pos, second_pos = split[0], split[1].replace(":", "")
        if second_pos in markov[first_pos]:
            markov[first_pos][second_pos] = markov[first_pos][second_pos] + freq
            if first_pos in markov[second_pos]:
                markov[second_pos][first_pos] = markov[second_pos][first_pos] + freq
            else:
                markov[second_pos][first_pos] = freq
        else:
            markov[first_pos][second_pos] = freq
            if first_pos in markov[second_pos]:
                markov[second_pos][first_pos] = markov[second_pos][first_pos] + freq
            else:
                markov[second_pos][first_pos] = freq

with open('../json/pos-transitions.json', 'w') as outfile:
    json.dump(markov, outfile)

print(markov)

