# BeautifulSoup parser for reading file
from bs4 import BeautifulSoup

# Open html file and pass it to BeautifulSoup to be parsed, then close the html file
file = open('twitter-trump.html')
soup = BeautifulSoup(file.read, 'html.parser')
file.close()

# Separate the tweets out from the rest of the html file.
tweets = soup.find_all(class_='js-tweet-text-container')

# Appends to a file the text of each tweet from the html file.
output = open('trump_tweets.txt', 'a')
for tweet in tweets:
    output.write(tweet.text)

# Close the output file
output.close()

def getText(url):
    file = open(url)
    soup = BeautifulSoup(file.read, 'html.parser')
    file.close()

    # Separate the tweets out from the rest of the html file.
    tweets = soup.find_all(class_='js-tweet-text-container')

    # Appends to a file the text of each tweet from the html file.
    output = open('trump_tweets.txt', 'a')
    for tweet in tweets:
        output.write(tweet.text)

    # Close the output file
    output.close()
