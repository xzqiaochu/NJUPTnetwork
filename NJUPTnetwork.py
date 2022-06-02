from inc.api import *
import sys
import time

username = sys.argv[1]
password = sys.argv[2]
while True:
    try:
        ip = getIP()
        if checkIP(ip) == False:
           login(username, password)
    except:
        pass
    time.sleep(5)
