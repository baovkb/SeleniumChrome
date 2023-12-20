import http.client as httplib
import time, subprocess

class DetectNetwork():
    def __new__(self):
        shell = subprocess.Popen('netsh mbn show profiles', shell=True, stdout=subprocess.PIPE)
        shell.wait()
        res = str(shell.stdout.read())
        shell.terminate()
        if res.find("There is no Mobile Broadband interface") > -1: #mobile network is enable
            # result = subprocess.run(['netsh', 'interface', 'show', 'interface'], shell=True, stdout=subprocess.PIPE)
            # res = result.stdout.decode('utf-8').replace('\r', '')
            # res = res.split('\n')
            # while ('' in res):
            #     res.remove('')
            # for item in res:
            #     if (item.find('Wi-Fi') != -1) and (item.find('Connected')) != -1:
                    # name = ''
                    # for tmp in range(item.find('Wi-Fi'), len(item)):
                    #     name = name + item[tmp]
            return Wifi()
        else: 
            shell = subprocess.Popen('netsh wlan disconnect', shell=True)
            shell.wait()
            shell.terminate()
            return Cellular()
        
class Network():
    def isConnect(self):
        conn = httplib.HTTPSConnection("8.8.8.8", timeout=1.5)
        try:
            conn.request("HEAD", "/")
            return True
        except:
            return False
        finally:
            conn.close()
    def connect(self): pass
    def disconnect(self): pass
    def changeIP(self): pass

class Wifi(Network): 
    def __init__(self) -> None:
        super().__init__()

class Cellular(Network):
    def __init__(self) -> None:
        shell = subprocess.Popen('netsh mbn show profiles', shell=True, stdout=subprocess.PIPE)
        res = str(shell.stdout.read())
        if res.find("There is no Mobile Broadband interface") > -1:
            print("Cellular is not available")
            return -1

        st = res.find("Cellular")
        name_cellular = ''
        while res[st] != ':':
            name_cellular += res[st]
            st = st + 1
        shell.terminate()
        self.name_cellular = name_cellular
        self.name_profile = '{2D591E2D-3C44-43BB-AF41-2FAB16FADA9B}' #profile tu tao, tao bang phan mem Windows Imaging and Configuration Designer (WICD)
        
    def connect(self):
        shell = subprocess.Popen('netsh mbn connect interface="%s" connmode=name name=%s' %(self.name_cellular,self.name_profile), shell=True, stdout=subprocess.PIPE)
        shell.wait()
        shell.terminate()

    def disconnect(self):
        shell = subprocess.Popen('netsh mbn disconnect interface="%s"' %self.name_cellular, shell=True, stdout=subprocess.PIPE)
        shell.wait()
        shell.terminate()

    def changeIP(self):
        self.disconnect()
        time.sleep(0.5)
        self.connect
        while not self.isConnect():
            self.connect()
            time.sleep(0.5)