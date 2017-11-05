#these following two import statements are for making the web requests and 
#parsing the JSON responces from telegram into Python dictionaries
import json 
import requests
import time
import urllib
import nltk
import generate_sentence
import find_pos
import transitions

#unique token to represent the echobot 
TOKEN = "479176894:AAHvXzZBhfh9YG9URDpn9SE9CoTQcx28xRc"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
#the url we must access in order to access the bot




#The following section simply reads the txt files
file = open("../txt/bigram_counts.txt", "r",encoding="utf-8")
bigram_counts = file.read()

file = open("../txt/trump-pos-corpus.txt", "r",encoding="utf-8")
trump_pos_corpus = file.read()

#file = open("../txt/trump_tweets.txt", "r",encoding="utf-8")
#trump_tweets = file.read()

file = open("../txt/trump_tweets_pos.txt", "r",encoding="utf-8")
trump_tweets_pos = file.read()



#this simply downloads the content from the url so that the json data can be loaded  
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

#loads the content returned into a Python dictionary
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

#get
def get_text_from_url(url):
    tweet_text_grabber.getText(url)


#This get all updates from the chat. We are able to provide clean return data to view
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

#this is to get the last update so that the chat shows the text message that the user wrote
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

#given the text message and te chat_id of the chat, we can send the message to the bot
def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            mainWord, mainPOS, POS_Order = findMain(text, chat)            
        except Exception as e:
            print(e)

            
def findMain(text, chat):            
    word_pos = nltk.pos_tag(nltk.word_tokenize(text))
    mainWord = ''
    mainPOS = ''
    POS_Order  = []
    
    for i in range(0, len(word_pos)):
        if 'NN' in word_pos[i][1]:
            mainWord = word_pos[i][0]
            mainPOS = word_pos[i][1]
            #send_message('Main word is ' + mainWord, chat)
            #send_message('Main POS is ' + mainPOS, chat)
            break
            
    for i in range(0, len(word_pos)-1):
        POS_Order.append( (word_pos[i][1], word_pos[i+1][1]) )
        
    
    valu = find_pos.best_pos(POS_Order)
    PoS_seq = transitions.transition(valu)
    sentence = generate_sentence(PoS_seq)
    #send_message(str(POS_Order), chat)
    #send_message(valu, chat)
    send_message(sentence, chat)
    
    return mainWord, mainPOS, POS_Order

#when the file is called in terminal, activate the bot
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()