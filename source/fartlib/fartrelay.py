from bs4 import BeautifulSoup
import os
import time
import random
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

class newest_art():
    def get_art(self, art=FartDir+newest_art_name):
        with open(art) as art:
            return art.read()
    def get_name(self):
        return newest_art_name
            
class random_art():    
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
    def get_art(self):
        with open(FartDir+self.art) as choice:
            return choice.read()
    def get_name(self):
        return self.art
        
            
class find():
    art_found = False
    item_match = ''
    def __init__(self, art):
        self.art = art.lower()
        if ".txt" not in self.art:
            self.art = self.art + ".txt"
        for item in local_art:
            if self.art in item.lower():
                if item.lower() in self.art:
                    self.art_found = True
                    self.item_match = item
                    break
        if not self.art_found:
            raise AttributeError(art+": This ascii art couldn't be found.")
    def get_art(self):
        with open(FartDir+self.item_match) as art:
            return art.read()
    def get_name(self):
        if not self.art_found:
            return "???"
        else:
            return self.item_match
