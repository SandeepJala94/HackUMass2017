# BeautifulSoup parser for reading file
from bs4 import BeautifulSoup
import re
import csv
import codecs

# Open html file and pass it to BeautifulSoup to be parsed, then close the html file
file_obj = open('politico-trump.html','r')
html = file_obj.read()
soup = BeautifulSoup(html, 'html.parser')
file_obj.close()

# Separate the tweets out from the rest of the html file.

p_in_story_text = soup.find("div", { "class" : "story-text" }).find_all("p")

dialougue = []

r='[A-Z]*[:]{1}.*'

for p in p_in_story_text:
    text = p.contents[0]


    try:
        match = re.search(r, text)
        if match:
            dialougue.append(text)
    except Exception:
        continue

trump_lines=[]
other_lines=[]

trump = "TRUMP:"
tr = []
ot = []
for d in dialougue:
    match = re.search('[A-Z]*[:]{1}', d)
    if match:
        speaker = match.group()
        speaker_line = d.split(speaker)[1]
        if trump in speaker:
            tr.append(speaker_line)
            trump_lines.append(tr)
            other_lines.append(ot)
            ot,tr = [], []
        else:
            ot.append(speaker_line)

other_line_sets=[]

count = len(other_lines)

for i in range(count):
    if(len(other_lines[i])<6):
        extra_slots = 6-len(other_lines[i])
        while(extra_slots>0):
            extra_slots-=1
            other_lines[i].append("")
        other_lines[i].append(trump_lines[i][0])

dialougues = []

for dialogue in other_lines:
    temp = []
    for line in dialogue:
        temp.append(line)
    dialougues.append(temp)

with open("dialougues.csv", "w",encoding="utf-16LE") as f:
    writer = csv.writer(f)
    writer.writerows(dialougues)
