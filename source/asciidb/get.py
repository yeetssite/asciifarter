from os import path
from os import environ
fartDir = environ["HOME"]+"/Documents/.asciiFarter"

def sources(sourceList=fartDir+"/sources.list"):
    with open(sourceList) as s:
        source_urls = list()
        for line in s:
            if line.strip(" ") != "":
                source_urls.append(line.strip("\n"))
        
    return(source_urls)
