# Find common linguistic patterns
# in Donald Trump Tweets

# Get the contents of the file
# Delimit by spaces and grab the last element
f = open('./trump_tweets_pos.txt', 'r')

# Make a list of pos
pos_lines = []

# make a list of pos in tweets
tweet_patterns = []

# Make a dictionary with the pos as the key and the item
# as a list of words associated with the pos
words = dict()

# Loop through all of the pos data
for i, pos in zip(range(100), f):
    print("i:", i, ",", pos)
    # Delimit the line by space
    line_split = pos.split(" ")
    # Get the word
    word = line_split[0]
    # Get the pos
    part_of_speech = line_split[-1].replace("\n", "")
    # Determine if the part of speech is a key in the dictionary
    # see if the word exists in the dictionary and the word is
    # not a link or @ or #
    if part_of_speech in words and not word.__contains__(".com") \
            and not word.__contains__("@")\
            and not word.__contains__("#"):
        words[part_of_speech].append(word)
    else:
        if not word.__contains__(".com") \
           and not word.__contains__("@") \
           and not word.__contains__("#"):
            words[part_of_speech] = [word]
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

#print(pos_lines)
print("Tweet Patterns: ", tweet_patterns)
#print('\n')
#print(words)


bigram_pos_counts = dict()

for tweet in tweet_patterns:
    for i in range(len(tweet)-1):
        bigram_pos = (tweet[i], tweet[i+1])
        if bigram_pos in bigram_pos_counts:
            bigram_pos_counts[bigram_pos] += 1
        else:
            bigram_pos_counts[bigram_pos] = 1

print()
print(bigram_pos_counts)
