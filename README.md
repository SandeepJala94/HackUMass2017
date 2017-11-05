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
1. Scrape the internet for Trump's tweets and interview
responses. This data is used to fill TrumpBot's vocabulary.

2. After finding sources, we used BeautifulSoup to find the
desired html elements from the webpages and collected them
into a text file.

3. We then passed the collected data to a python script that
uses nltk to separate each word and label it's part of 
sentence (i.e. noun, verb, adjective, etc.).

4. The data is then passed to another python script where it
is cleared of any extraneous data such as *urls* or special
characters.

Data
====
HTML
----
All *HTML* files are stored in the *html* folder. 
The webpages were scraped to gather information for
the chatbot.

### HTML source files
-politico-trump.html
-twitter-trump.html

PYTHON
------
Python is used extensively to gather data from websites.
Python scripts are then used to parse and clean the data
from it's original source.

### Libraries
-Selenium
-BeautifulSoup
-nltk

TEXT FILES
----------
The text files contain the parsed data from
each step of data collection process.
