import os, sys 
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0, parent_dir)  

from inc.hack import *

ACCOUNT_FILE = "hack/record/account.txt"
RECORD_FILE = "hack/record/hack.txt"

def checkRecord(account):
    with open(RECORD_FILE, "r") as f:
        hacks = f.readlines()
    return account + "\n" not in hacks

def record(account):
    with open(RECORD_FILE, "a") as f:
        f.write("%s\n" % account)

def HackAccount(account):
    if checkRecord(account) and hack(account):
        record(account)

with open(ACCOUNT_FILE, "r") as f:
    lines = f.readlines()
for line in lines:
    account = line.strip()
    print(account)
    HackAccount(account)
