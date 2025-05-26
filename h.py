import time

def getPlus ():
    print('+++', end='')
    time.sleep(0.2)
    print('\r', end='')

def getMinus ():
    print('---', end='')
    time.sleep(0.2)
    print('\r', end='')

while True:
    getMinus()
    getPlus()