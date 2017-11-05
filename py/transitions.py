# Make a markov model based on the bigram_counts.txt file

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
    line = l
    split = line.split(" ")
    pos_trans, freq = split[0], split[1]
    split = pos_trans.split(",")
    first_pos, second_pos = split[0], split[1]
    for markov_element in markov[first_pos]:
        if markov_element[0] == second_pos:
            markov_element = (second_pos, markov_element[1] + freq)
            isfound = True
            break

    if not isfound:
        markov[first_pos].append((first_pos, freq))
        isfound = False

    for markov_element in markov[second_pos]:
        if markov_element[0] == first_pos:
            markov_element = (second_pos, markov_element[1] + freq)
            isfound = True
            break

    if not isfound:
        markov[second_pos].append((second_pos, freq))
        isfound = False

print(markov)


