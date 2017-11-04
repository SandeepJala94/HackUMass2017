# ------------------------------------------
# Author: Ian Torres
# University: UMASS Amherst
# Affiliation: UVA (DREU CRA-W 2017)
# Program: LevanScraper.py
# ------------------------------------------

# ------------------------------------------
# This script is meant to download all query
# results from the levan web page.
# Many of these values are hardcoded because
# it seems these values are not dynamically
# named. However, this may change so keep this
# in mind.
#
#
# Also, please read all of the comments
# provided in this program, so you fully
# understand what it does.
# ------------------------------------------

# ------------------------------------------
# Import necessary modules:
#
# selenium.webdriver: used to control a
# browser window
#
# bs4.BeautifulSoup: used to parse html
# elements and grab important contents
#
# time: used to make the program sleep at
# certain instances to simulate human
# behavior on a browser
#
# random: randomize timings of human
# behavior
# ------------------------------------------
from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path
import time
import random as ran
import traceback


# ------------------------------------------
# Establish a connection to:
# http://levan.cs.washington.edu
# with selenium to load dynamic web page
# content.
#
#
# Note in order to run this program the
# (geckodriver) directory must be in the
# PATH environment variable
# ------------------------------------------
def scrapelevan(searchterm):
    term = searchterm.rstrip().lstrip()  # trim any leading or trailing spaces
    # print('Term -> ', term)
    # check to see if a single value was input
    try:
        browser_levan = webdriver.Firefox()  # Open a web browser (Firefox)
        if term.__contains__(' '):
            # Print an error message
            print('\033[1;31;40mOnly single value search terms:\033[m')
            search_terms = term.split(' ')
            print('\033[1;31;40m%s\033[m\n' % " \n".join(search_terms))
            print('\033[1;31;40mClosing the browser...\033[m')
            browser_levan.close()
            return 0
        try:
            seconds = 1 + int(ran.random() * 5)  # Make sure it doesn't look like a web scraper
            time.sleep(seconds)  # Wait for the browser to open
            browser_levan.get('http://levan.cs.washington.edu')
            seconds = 1 + int(ran.random() * 5) # Make sure it doesn't look like a web scraper
            time.sleep(seconds)
            # Get the submit button location
            submit_button = browser_levan.find_element_by_id('submit-button').\
                find_element_by_partial_link_text('Add Concepts')
            submit_button.click()  # click the submit button
            seconds = 1 + int(ran.random() * 5)  # Make sure it doesn't look like a web scraper
            time.sleep(seconds)
            text_field = browser_levan.find_element_by_name('concept')  # Get the text field
            text_field.clear()  # Clear text field of any words
            text_field.send_keys(term)  # Input the search term in the text box
            # Get the new submit button on the page
            submit_button = browser_levan.find_element_by_xpath("//input[@value='Submit'][@type='submit']")
            seconds = 1 + int(ran.random() * 5)  # Make sure it doesn't look like a web scraper
            time.sleep(seconds)
            submit_button.click()
            # -----------------------------------------------------------------------
            seconds = 1 + int(ran.random() * 5)  # Make sure it doesn't look like a web scraper
            time.sleep(seconds)
            # Get the results page of the levan query
            selector = browser_levan.find_element_by_partial_link_text('...[view all discovered concept relationships]')
            seconds = 1 + int(ran.random() * 5)  # Make sure it doesn't look like a web scraper
            time.sleep(seconds)
            selector.click()
            seconds = 1 + int(ran.random() * 5)  # Make sure all web contents are loaded to the browser
            time.sleep(seconds)
            page_content = browser_levan.page_source  # Get the dynamically rendered content of the web page
            browser_levan.close()  # Close the browser window
            return page_content  # Return the page contents
        except:
            print('\033[1;31;40mClosing the browser...\033[m')
            browser_levan.close()
            print('\033[1;31;40mPage element(s) were not able to be found...\033[m')
            print('\033[1;31;40mLast Exception:\033[m')
            traceback.print_exc()
            return 0
    except:
        print('\033[1;31;40mBrowser unable to open...\033[m')
        print('\033[1;31;40mGeckodriver may not be configured to PATH env variable\033[m')
        print('\033[1;31;40mPlease check PATH (prompt> echo $PATH)\033[m')
        print('\033[1;31;40mThe directory which the driver is located in should be configured\n'
              'to the PATH env variable\033[m')
        traceback.print_exc()
        return 0

# ------------------------------------------
# This function is used to parse the dynamic
# content generated by scrapelevan
# ------------------------------------------
def parselevan(query, page_content):
    print('\033[1;32;40mSuccess!\033[m')
    print('\033[1;32;40mNow loading %s n-grams...\033[m' % query)
    soup = BeautifulSoup(page_content, 'html.parser')  # Parse the html document
    chair_ngrams_lists = soup.find_all(class_='n-gram-similar-word-list')  # Grab the ngram containers
    # Unpack the ngram containers into lists
    chair_ngrams_lists_elements = [c.find_all('li') for c in chair_ngrams_lists]
    # Grab all of the ngram list items
    chair_ngram_text = [col.get_text() for row in chair_ngrams_lists_elements for col in row]
    return chair_ngram_text

query = 'chair'
page = scrapelevan(query)


# ------------------------------------------
# Main Script (Pseudo main method)
# ------------------------------------------

# If scrapelevan successfully got the dynamic content
if page != 0:
    # Scrape the import information we want: n-grams
    get_text = parselevan(query, page)
    # designate a file title (make it plural since there are many n-grams
    query += 's.txt'
    # establish the current direct as the place where the file will be saved
    query_file_path = './' + query
    query_file = Path(query_file_path)  # Check to see if the file already exists
    if query_file.exists():
        # Give the user the chance to accept or reject overwriting the file
        print('This query file already exists: %s' % query_file_path)
        # user input
        option = input('Do you wish to overwrite it? (y/n): ').lstrip().rstrip()
        if option.lower() == 'y':
            # Erase the file contents
            open(query_file_path, 'w').close()
            # Open the file to be written to
            f = open(query_file_path, 'w')
            # write the n-grams to the file iteratively
            for c in get_text:
                line = c + '\n'
                f.write(line)
            f.close()
        else:
            print("Scraping program has not overwritten the file %s" % query_file_path)