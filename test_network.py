
import requests, time, subprocess
    
def turnOffDcom():
    subprocess.Popen('netsh mbn disconnect interface="Cellular"', shell=True, stdout=subprocess.PIPE).stdout.read()


def turnOnDcom():
    for i in range(0, 3):
        shell = subprocess.Popen('netsh mbn connect interface="Cellular" connmode=name name={E36F2B0D-EB98-44EB-ABDC-A96AF8C2B052}', shell=True, stdout=subprocess.PIPE).stdout.read()
        shell = str(shell)
        if (shell.find('The given interface is not present or not a Mobile Broadband interface') != -1):
            input('Chua ket noi dcom')
        elif (shell.find('Connect Failure') != -1):
            turnOffDcom()
            continue
        break

def isDcom():
    shell = subprocess.Popen('netsh mbn show profiles', shell=True, stdout=subprocess.PIPE).stdout.read()
    shell = str(shell)
    if shell.find('There is no Mobile Broadband interface') != -1:
        return False
    return True



if (isEthernet() == True):
    print('Dung dcom')
else: print('Khong dung dcom')
    

