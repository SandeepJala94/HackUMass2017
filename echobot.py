import json 
import requests
import time
import urllib
import nltk

TOKEN = "479176894:AAHvXzZBhfh9YG9URDpn9SE9CoTQcx28xRc"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


file = open("../txt/trump_tweets_pos.txt","r")
trump_tweets_pos = file.read() 

file = open("../txt/trump-pos-corpus.txt", "r")
trump_pos_corpus = file.read()

file = open("../txt/bigram_counts.txt", "r")
bigram_counts = file.read()

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_text_from_url(url):
    tweet_text_grabber.getText(url)


#def get_updates():
    #url = URL + "getUpdates"
    #js = get_json_from_url(url)
    #return js

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


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


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:
            print(e)
    
    
    
def analyzeString(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            newText = 'length of text is ' + str(len(text))
            send_message(newText, chat)
            mainWord, mainPOS, POS_Order = findMainTopic_POS(text, chat)
            #buildSentenceWithMainWord(mainWord, mainPOS)
        except Exception as e:
            print(e)
    
    
def findMainTopic_POS(text, chat):
    word_pos = nltk.pos_tag(nltk.word_tokenize(text))
    mainWord = ''
    POS_Order = []
    
    for i in range(0, len(word_pos)):
        if 'V' in word_pos[i][1] or 'N' in word_pos[i][1]:
            mainWord = word_pos[i][0]
            mainPOS = word_pos[i][1]
            #i = len(word_pos)+1
            send_message(str('Main word is ' + word_pos[i][0]), chat)
            send_message(str('Main POS is ' + word_pos[i][1]), chat)
            break
    
    
    for i in range(0, len(word_pos)):
        POS_Order.append(word_pos[i][1])
        
    send_message(str(POS_Order), chat)
    return mainWord, mainPOS, POS_order
    #send_message(str(len(word_pos)), chat)
    
    


    
    
#def buildSentenceWithMainWord(mainWord, mainPOS):
    
    
    
    
    
    
    
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            analyzeString(updates)
            #echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()