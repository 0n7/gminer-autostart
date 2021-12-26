import win32api, time
from subprocess import Popen
import os
def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0 # Get inactive time.


def ifinactive():
    while True:
        if mode == 1:
            Popen("mine_eth.bat")
            mode == 0
            print("Start mine_eth.bat") # Start miner.
            nowactive()
            break

def inactive_check():
    global mode
    while True:
        if getIdleTime() < 900: # 900 sec = 15 min.
            time.sleep(5) # every 5 sec checking.
            print("wait - ",getIdleTime(),"/","900",sep="")
        else:
            mode = 1
            ifinactive()
            break

def nowactive():
    while True:
        if getIdleTime() < 1:
            print("stop miner.exe")
            os.system("taskkill /f /im  miner.exe")
            break
    inactive_check()

inactive_check()