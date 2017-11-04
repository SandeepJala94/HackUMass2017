# Find common linguistic patterns
# in Donald Trump Tweets

# Get the contents of the file
# Delimit by spaces and grab the last element
f = open('./trump_tweets_pos.txt', 'r', encoding = 'utf-8')

# Make a list of pos
pos_lines = []

# make a list of pos in tweets
tweet_patterns = []

# Make a dictionary with the pos as the key and the item
# as a list of words associated with the pos
words = dict()
isfound = False

# Loop through all of the pos data
for pos in f:
    # Delimit the line by space
    line_split = pos.split(" ")
    # Get the word
    word = line_split[0].lower()
    # Get the pos
    part_of_speech = line_split[-1].replace("\n", "")
    # Determine if the part of speech is a key in the dictionary
    # see if the word exists in the dictionary and the word is
    # not a link or @ or #
    if part_of_speech in words \
            and not word.__contains__(".*:\/\/.*") \
            and not word.__contains__(".*\..*\..*\/.*") \
            and not word.__contains__(".*@.*\..*")\
            and not word.__contains__("@")\
            and not word.__contains__("#")\
            and not word.__contains__("[\+]?[\d]*[\.|\-]?[(]?[\d]{3}[)]?[\.|\-]*[\d]{3}[\.|\-]*[\d]{4}"):
        for j, tup in enumerate(words[part_of_speech]):
            if word == tup[0]:
                words[part_of_speech][j] = (word, tup[1] + 1)
                isfound = True
                break
            else:
                isfound = False

        if not isfound:
            words[part_of_speech].append((word, 1))
            isfound = False

    else:
        if not word.__contains__(".*:\/\/.*") \
           and not word.__contains__(".*\..*\..*\/.*") \
           and not word.__contains__(".*@.*\..*")\
           and not word.__contains__("@") \
           and not word.__contains__("#") \
           and not word.__contains__("[\+]?[\d]*[\.|\-]?[(]?[\d]{3}[)]?[\.|\-]*[\d]{3}[\.|\-]*[\d]{4}"):
            words[part_of_speech] = [(word, 1)]
    pos_lines.append(part_of_speech)


# Make a temporary list to hold individual tweet patterns
temp = []
for p in pos_lines:

    # See if the tweet ended
    if p == ".":
        # add the tween pattern to the list
        tweet_patterns.append(temp)
        # clear the temporary list
        temp = []
    else:
        temp.append(p)

# print(pos_lines)
# print("Tweet Patterns: ", tweet_patterns)
# print('\n')
# print(words)


bigram_pos_counts = dict()

for tweet in tweet_patterns:
    tweet = [pos for pos in tweet if pos in ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']]
    for i in range(len(tweet)-1):
        bigram_pos = (tweet[i], tweet[i+1])
        if bigram_pos in bigram_pos_counts:
            bigram_pos_counts[bigram_pos] += 1
        else:
            bigram_pos_counts[bigram_pos] = 1

print()
print(bigram_pos_counts)
f.close()

for pos in words:
    words[pos].sort(key=lambda e: -e[1])

f = open('trump-pos-corpus.txt', 'w')

for pos in words:
    f.write(pos + ":" + str(words[pos]) + '\n\n')

f.close()

bigram_counts_file = open('bigram_counts.txt', 'w')
output = ''
for count in bigram_pos_counts:
    output = count[0] + ',' + count[1] + ': ' + str(bigram_pos_counts[count]) + '\n'
    bigram_counts_file.write(output + "\n")
    # print(output)
    # bigram_counts_file.write(output)
bigram_counts_file.close()
print("done")

