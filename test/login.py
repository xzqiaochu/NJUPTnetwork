import os, sys 
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0, parent_dir)  

from inc.api import *

username = ""
password = ""
login(username, password)
ip = getIP()
print(ip, checkIP(ip))