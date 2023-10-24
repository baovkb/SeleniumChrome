import http.client as httplib
import requests, time, subprocess

Viettel = '{E36F2B0D-EB98-44EB-ABDC-A96AF8C2B052}'
Vina = '{2D591E2D-3C44-43BB-AF41-2FAB16FADA9B}'

def isConnect():
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=1.5)
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False
    finally:
        conn.close()

def resetNetWork():
    #for i in range(0, 3):
    #    if isConnect() == True: break
    #    else:
    #    #do something
            pass

def changeIp(api):
    try:
        request = requests.get('https://proxymmo.net/api/proxy/get-new-proxy?api_key=%s' %api).json()
        while request['status'] == 'error':
            delay = request['message'].replace('Vui lòng chờ', '')
            delay = delay.replace('giây để thực hiện lại', '')
            delay = delay.replace(' ', '')
            print('Doi %s s' %delay)
            time.sleep(int(delay) + 0.5)
            request = requests.get('https://proxymmo.net/api/proxy/get-new-proxy?api_key=%s' %api).json()

        new_proxy = str(request['data']['public_ip']) + ':' + str(request['data']['http_port'])
        return new_proxy 
    except: return '0.0.0.0:00'

def isEthernet():
    shell = subprocess.Popen('ipconfig /all', shell=True, stdout=subprocess.PIPE).stdout.read()
    shell = str(shell)
    if shell.find('Ethernet adapter Ethernet') != -1:
        return True
    return False

def isDcom():
    shell = subprocess.Popen('netsh mbn show profiles', shell=True, stdout=subprocess.PIPE).stdout.read()
    shell = str(shell)
    if shell.find('There is no Mobile Broadband interface') != -1:
        return False
    return True

def turnOffDcom():
    subprocess.Popen('netsh mbn disconnect interface="Cellular"', shell=True, stdout=subprocess.PIPE)

def turnOnDcom():
    for i in range(0, 3):
        shell = subprocess.Popen('netsh mbn connect interface="Cellular" connmode=name name=%s' %Vina, shell=True, stdout=subprocess.PIPE).stdout.read()
        shell = str(shell)
        if (shell.find('The given interface is not present or not a Mobile Broadband interface') != -1):
            input('Chua ket noi dcom')
        elif (shell.find('Connect Failure') != -1):
            turnOffDcom()
            continue
        break

def changeIpDcom():
    turnOffDcom()
    time.sleep(1.5)
    while isConnect() == False:
        turnOnDcom()
        time.sleep(1.5)