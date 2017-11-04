# Natural Language Tool Kit to label parts of speech(PoS)
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

# Import tweet text
file = open('trump_tweets.txt')
text = file.read()

# Separate the words and label the PoS
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)

# Output to text file
with open('trump_tweets_pos.txt', 'a') as fp:
    fp.write('\n'.join('%s %s' % x for x in tagged_tokens))
