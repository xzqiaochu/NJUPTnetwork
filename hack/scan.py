import os, sys 
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0, parent_dir)  

from inc.api import *

IP_FILE = "hack/record/ip.txt"
ACCOUNT_FILE = "hack/record/account.txt"

def scan(ip):
    accout = checkIP(ip)
    if accout:
        with open(IP_FILE, "a") as f:
            f.write("%s\n" % ip)
        with open(ACCOUNT_FILE, "a") as f:
            f.write("%s\n" % accout)

for i in range(128, 256):
    for j in range(0, 256):
        ip = "10.162.%s.%s" % (i, j)
        print(ip)
        try:
            scan(ip)
        except:
            pass