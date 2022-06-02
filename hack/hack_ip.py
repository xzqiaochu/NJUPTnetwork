import os, sys 
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0, parent_dir)  

from inc.hack import *

IP_FILE = "hack/record/ip.txt"
RECORD_FILE = "hack/record/hack.txt"

def checkRecord(account):
    with open(RECORD_FILE, "r") as f:
        hacks = f.readlines()
    return account + "\n" not in hacks

def record(account):
    with open(RECORD_FILE, "a") as f:
        f.write("%s\n" % account)

def HackIP(ip):
    account = checkIP(ip)
    if account and checkRecord(account) and hack(account):
        record(account)

with open(IP_FILE, "r") as f:
    lines = f.readlines()
for line in lines:
    ip = line.strip()
    print(ip)
    HackIP(ip)
