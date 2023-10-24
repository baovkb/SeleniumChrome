from pickle import TRUE
import subprocess

def openTele(indexProfile):
    try:
        path = 'D:\\MMO\\AMA\\telegram\\' + str(indexProfile) + '\\Telegram.exe'
        return subprocess.Popen(path,creationflags=0x00000008)
    except: pass

def closeTele(process):
    if process is not None:
        process.terminate()
        return None