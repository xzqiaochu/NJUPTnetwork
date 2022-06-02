from inc.api import *

HACK_PASS = "123456"

def hack(account):
    loginOutMyself()
    login(account, HACK_PASS)
    return checkIP(getIP())
