import requests
import re

def getIP():
    url = "http://10.10.244.11/"
    res = requests.get(url = url)
    res.encoding = 'gbk'
    ip = re.search("v46ip=\'([^\']*)\'", res.text).group(1)
    return ip

def checkIP(ip):
    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=checkScanIP&wlanuserip=%s" % (ip)
    res = requests.get(url = url)
    status = re.search('\"result\":\"([^\"]*)\"', res.text).group(1)
    if (status == 'ok'):
        account = re.search('\"account\":\"([^\"]*)\"', res.text).group(1)
        return account
    else:
        return False

def login1(username, password):
    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150"
    data = {"DDDDD": ",0,%s" % username, "upass": password}
    requests.post(url = url, data = data)

def login2(username, password):
    url = "http://192.168.168.168/"
    data = {"DDDDD": username, "upass": password, "0MKKey": ""}
    requests.post(url = url, data = data)

def login(username, password):
    login1(username, password)
    login2(username, password)

def loginOutAccount(account):
    url = "http://10.10.244.11:801/eportal/?c=IsOnline&a=logout&account=%s" % account
    requests.get(url = url)

def loginOutIP(ip):
    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Logout&wlanuserip=%s" % ip
    requests.get(url = url)

def loginOutMyself():
    while checkIP(getIP()):
        loginOutAccount(checkIP(getIP()))
        # loginOutIP(getIP())