from bs4 import BeautifulSoup
import os
import time
import random
from sys import stdout
screen_size = os.get_terminal_size()
screen_chars = screen_size.lines * screen_size.columns
FartDir = os.environ['HOME'] + "/Library/.asciiFarter/art/"
local_art = os.listdir(FartDir)
for item in local_art:
    if item.endswith('.txt'):
        pass
    else:
        local_art.remove(item)

with open(FartDir+"status.xml") as status:
    status = status.read()
    fartSoup = BeautifulSoup(status, 'xml')
    newest_art_name = fartSoup.find('NewestArt').text
    newest_art_name = newest_art_name.replace('asciiArt/', '')

def newest_art(art=FartDir+newest_art_name):
    with open(art) as art:
        for line in art.read():
            stdout.write(line)
            time.sleep(0.0005)
            stdout.flush()

def random_art():
    displayable = False
    while not displayable:
        art = random.choice(local_art)
        art_good_size = True
        with open(FartDir+art) as choice:
            for line in choice:
                if len(line) > screen_size.columns:
                    art_good_size = False
                    break
        if art_good_size:
           displayable = True
        else:
           continue
    with open(FartDir+art) as art:
        for line in art.read():
            stdout.write(line)
            time.sleep(0.0005)
            stdout.flush()

def find(art):
    art = art.lower()
    if ".txt" not in art:
        art = art + ".txt"
    print('[33mSearching for [1;34m"'+art+'"[0;33m...[m')
    art_found = False
    item_match = ''
    for item in local_art:
        if art in item.lower():
            if item.lower() in art:
                art_found = True
                item_match = item
                break
    if art_found:
        print('[47;1;34m'+item_match+':[0m')
        with open(FartDir+item_match) as art:
            for line in art.read():
                stdout.write(line)
                time.sleep(0.0005)
                stdout.flush
    else:
        print('[31mSorry, but I was unable to find [1;34m"'+art+'"[0;31m.[m')
        


