import http.client as httplib
import requests, time, subprocess

Viettel = '{E36F2B0D-EB98-44EB-ABDC-A96AF8C2B052}'
Vina = '{2D591E2D-3C44-43BB-AF41-2FAB16FADA9B}'

class Cellular():
    def __init__(self) -> None:
        shell = subprocess.Popen('netsh mbn show profiles', shell=True, stdout=subprocess.PIPE)
        res = str(shell.stdout.read())
        if res.find("There is no Mobile Broadband interface") > -1:
            print("Cellular is not available")
            exit(-1)

        st = res.find("Cellular")
        name_cellular = ''
        while res[st] != ':':
            name_cellular += res[st]
            st = st + 1
        shell.terminate()
        self.name_cellular = name_cellular
        self.name_profile = '{2D591E2D-3C44-43BB-AF41-2FAB16FADA9B}'

    def isConnect(self):
        conn = httplib.HTTPSConnection("8.8.8.8", timeout=1.5)
        try:
            conn.request("HEAD", "/")
            return True
        except:
            return False
        finally:
            conn.close()
        
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