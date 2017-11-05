Donald Trump Chat Bot
=====================
Goal
----
The goal of this project is to create a chat bot
that will respond to the user in a manner that matches
Donald Trump.

We are using python to collect and parse data collected
from the internet.

Method
------
1. Use [Selenium][1] to scrape the internet for Trump's tweets 
and interview responses. This data is used to fill TrumpBot's
vocabulary.

2. After finding sources, we used [BeautifulSoup][2] to find the
desired html elements from the webpages and collected them
into a text file.

3. We then passed the collected data to a python script that
uses [NLTK][3] to separate each word and label it's part of 
sentence (i.e. noun, verb, adjective, etc.).

4. The data is then passed to another python script where it
is cleared of any extraneous data such as *urls* or special
characters. It is then organized by it's part of sentence (PoS) 
and iterations are added together.

Example of Adjectives:
`JJ:[('great', 118), ('many', 37), ('big', 32), ('much', 22), ('last', 21), ('good', 20), ('first', 19), ('american', 17), ('wonderful', 15), ('military', 15)]`

5. A relation dictionary is made from a PoS bigram count.
A list of 20 or less is created to be used as a random
word list. A word will be randomly chosen based on the
PoS and frequency of Trump's usage to create a sentence.

6. A user can now communicate with TrumpBot.


Data
====
HTML
----
All *HTML* files are stored in the *html* folder. 
The webpages were scraped to gather information for
the chatbot.

#### HTML source files
- [politico-trump.html](https://github.com/SandeepJala94/HackUMass2017/blob/master/html/politico-trump.html)
- [twitter-trump.html](https://github.com/SandeepJala94/HackUMass2017/blob/master/html/twitter-trump.html)


PYTHON
------
Python is used extensively to gather data from websites.
Python scripts are then used to parse and clean the data
from it's original source.

#### Libraries
- [Selenium][1]
- [BeautifulSoup][2]
- [NLTK][3]


TEXT FILES
----------
The text files contain the parsed data from
each step of data collection process.

[1]: http://www.seleniumhq.org/        "Selenium"
[2]: https://www.crummy.com/software/BeautifulSoup/  "BeautifulSoup"
[3]: http://www.nltk.org/    "NLTK"
