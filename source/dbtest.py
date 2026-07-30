import asciidb.get
import urllib.request, urllib.error
sources = asciidb.get.sources()
print("Checking "+str(len(sources))+" source(s) for connectivity...")
for source in sources:
    try:
        with urllib.request.urlopen(source+"status.xml"):
            print(source+"status.xml: [1;32mGood[0m")
    except (urllib.error.HTTPError,urllib.error.URLError):
        print(source+"status.xml: [1;31mBad[0m") 
