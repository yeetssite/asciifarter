import os
import time
for x in range(255):
    time.sleep(0.5)
    os.system("nslookup 192.168.0."+str(x))
