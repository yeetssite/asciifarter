# NOTE: This version is currently in alpha, and the way 
# AsciiFarter uses local art may change in future updates. 
#
# This version is simply a proof of concept, and only exists
# to help me figure out how to make this shih actually work.
import getfart
import os
import time
# Temporarily fixed art directory due to making this on a
# friggin iPhone. Might add the ability to change this
# depending on user option and system types (eg. normal Linux, 
# Termux, which is basically Linux on an Android phone, MacOS
# and Windows).
FartDir = os.environ["HOME"]+"/Library/.asciiFarter/art/"
def art_installer():
    # Downloads ascii arts to your device.
    broken = False
    while not broken: # run installer in a loop to retry attempts
        try:
            print("Installing art to "+FartDir)
            # keep XML file with art attributes and only
            # open it when needed.
            newest_art = getfart.newest_art()
            with open(FartDir+"status.xml", 'w') as status:
                status.write("<LocalArt>\n")
                status.write("  <NewestArt>"+newest_art.name+"</NewestArt>")
                status.write("\n</LocalArt>")
            local_arts = os.listdir(FartDir)
            # Check remote arts against list of existing local
            # arts:
            for r_art in getfart.art_list:
                r_art = r_art.replace("asciiArt/", '')
                # Show as "Installed" if a file with the same
                # name exists. Might do some checksum trickery
                # in the future to double-check.
                if r_art in local_arts:
                    print(r_art+": [32mInstalled.[m")
                    # Download the art if not installed
                    # by copying the text to a file.
                    # Might change so the file is copied
                    # Exactly instead.
                else: 
                    print(r_art+": [33mInstalling...[m")
                    l_art = getfart.find_art(r_art)
                    with open(FartDir+r_art, 'w') as artFile:
                        for line in l_art.text:
                            artFile.write(line)
                    print(r_art+" [32mInstalled.[m")
            broken = True
        except FileNotFoundError:
            os.mkdir(FartDir)
            continue
