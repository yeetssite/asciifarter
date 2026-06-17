#!/usr/bin/python
from fartlib import getfart, localfart, fartrelay, version, copyright
from sys import argv, exit
from os import path
import urllib

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
                print("[31mNo art to look for.[m")
            break
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
else:
       
