#!/usr/bin/python
from fartlib import getfart, localfart, fartrelay, version, copyright
from sys import argv, exit
from os import path
import urllib
import os
asciifart_version = 2.4

user_passed_args = False

try:
    if argv[1:]:
        argls = argv[1:]
        user_passed_args = True
except IndexError:
    argls = None

if user_passed_args:
    for i in range(len(argls)):
        if argls[i].lower() == "find":
            try:
                find_art = True
                searchq = argls[i+1]
            except IndexError:
                print("AsciiFarter find: [31mNo art to look for.[m")
                exit(1)
            break
        elif argls[i].lower() == "add":
            try:
                add_art = True
                art_path= argls[i+1]
                break
            except IndexError:
                print("AsciiFarter add: [31mNo art to add...[m")
                exit(1)
        elif argls[i].lower() == "random":
            random_art = True
            break
        elif argls[i].lower() == "newest":
            newest_art = True
            break
        elif argls[i].lower() == "version":
            print("AsciiFarter Version "+str(asciifart_version)+" Running on FartLib v"+str(version)+".")
            print(copyright)
            exit(0)
        elif argls[i].lower() == "update":
            update_art = True
            break

        elif argls[i].lower() == "help":
            print("""AsciiFarter 2 | Help
USAGE: asciiFarter2 [COMMAND]

COMMANDs:
    COMMAND | DESCRIPTION
    * random | Displays a random ascii art.
    * newest | Displays the newest ascii art.
    * find <ART> | Finds and displays the ascii art
                   named <ART>.
    * update | Update your local art library.
    * version | Displays version and copyright info.
    * help | Displays this help message.""")
            exit(0)
        elif argls[i].startswith("-"):
            continue
        else:
            print(argls[i]+": AsciiFarter doesn't know that Command.")


    try:
        if update_art:
            FartDir = os.environ['HOME'] + '/Library/.asciiFarter/art/'
            localfart.art_installer()
            newest_art = ''
            newest_art_mtime = 0
            for art in fartrelay.local_art:
                art_mtime = os.path.getmtime(FartDir)
                if 'asciiArt/'+ art not in getfart.art_list:
                    if art_mtime > newest_art_mtime:
                        newest_art_mtime = art_mtime
                        newest_art = art    
            localfart.add(newest_art)
            exit(0)
    except NameError:
        update_art = False
    try:
        if add_art:
            if not os.path.isfile(art_path):
                if not os.path.isdir(art_path):
                    art_path = './' + art_path
            print(art_path)
            FartDir = os.environ['HOME'] + '/Library/.asciiFarter/art/'
            if os.path.isfile(art_path):
                if art_path.endswith('.txt'):
                    with open(art_path) as art:
                        art_file = os.path.basename(art_path).strip('/')
                        with open(FartDir+art_file, 'w') as lib_art:
                            for line in art.read():
                                lib_art.write(line)
                    localfart.add(art_file)
                else:
                    print('AsciiFarter:[31m You can only Add ".txt" Files to your Art Library.[m')
                    exit(2)
            else:
                if not os.path.isdir(art_path):
                    print(art_path+': AsciiFarter could not Find this File.')
                    exit(2)
                else:
                    print(art_path+': AsciiFarter Currently only supports Adding Art Files individually.')
                    exit(2)
    except NameError:
        add_art = False
    
        
else:
    fart = getfart.random_art()
    fart.poop()

