from selenium import webdriver
import undetected_chromedriver as webdriver
import time, os, tabs
import IOFile as file
from tabs import Tabs

browser_path = r'D:\MMO\gologin\orbita-browser\chrome.exe'
user_data_path = r'D:\MMO\Gologin_tmp'
driver_path = r'.\chromedriver\chromedriver.exe'

class ProfileGL(Tabs):
    def __init__(self, *args) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = browser_path
        for arg in args:
            self.options.add_argument(arg)
        self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--disable-notifications')
        self.options.add_argument('--no-service-autorun')
        self.options.add_argument('--disable-features=ExtensionsToolbarMenu,ChromeLabs,ReadLater,TriggerNetworkDataMigration,ChromeWhatsNewUI,ViewportHeightClientHintHeader')

    def openGL(self, profile_id, proxy = ''):
        profile_path = os.path.join(user_data_path, str(profile_id))
        self.options.add_argument('--user-data-dir=%s' %(profile_path))
        self.profile_id = profile_id
        if proxy != '':
            infoProxy = proxy.split(':')
            if len(infoProxy) == 4:
                file.changeAuthyProxy(profile_id, username=infoProxy[2], password=infoProxy[3])
            elif len(infoProxy) == 2:
                file.changeAuthyProxy(profile_id)
            else: raise Exception
            self.options.add_argument('--proxy-server=%s' %(infoProxy[0] + ':' + infoProxy[1]))
            #options.add_argument('--proxy-server=proxy_username:proxy_password@proxy_ip:proxy_port')
        try:
            self.driver = webdriver.Chrome(driver_executable_path = driver_path, options = self.options)
            return self
        except: return None

    def closeGL(self):
        if self.driver is None:
            return None
        try:
            while len(self.driver.window_handles) > 0:
                try:
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.driver.close()
                except: pass
        except: pass
        try:
            time.sleep(1)
            self.driver.quit()
            pass
        except: pass
        return None

    def openMultiTab(self, listUrl: list):
        if len(listUrl) > 0:
            self.openTab(listUrl[0], True)
        j = 1
        while j < len(listUrl):
            self.openTab(listUrl[j], False)
            j = j + 1
        self.driver.switch_to.window(self.driver.window_handles[0])