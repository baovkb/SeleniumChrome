from selenium import webdriver
import undetected_chromedriver as webdriver
import time, copy, os
from selenium.webdriver.common.by import By
import network, IOFile as file
from pathlib import Path

browser_path = r'D:\MMO\Gologin\orbita-browser\chrome.exe'
user_data_path = r'D:\MMO\Gologin'
driver_path = r'.\chromedriver\chromedriver.exe'

class ProfileGL():
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = browser_path
        #self.options.add_argument('--load-extension=D:\\MMO\\Gologin\\extensions\Venom')
        #self.options.add_argument('--profile-directory=Default')
        self.options.add_argument('--load-extension=D:\\MMO\\Gologin\\extensions\Metamask')
        self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--disable-notifications')
        self.options.add_argument('--no-service-autorun')

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
        try:
            self.driver = webdriver.Chrome(driver_executable_path = driver_path, options = self.options)
        except: return None

    def openTab(self, url: str, isFirstTab = False):
        try:
            if isFirstTab == False:
                #driver.tab_new(url)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.execute_script("window.open()")
                self.driver.switch_to.window(self.driver.window_handles[-1])

            self.driver.get(url)
            time.sleep(0.5)
            if self.driver.current_url == 'chrome://new-tab-page/': 
                raise Exception('cannot open url')
        except: raise ValueError('url is invalid')

    def closeTab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    def selectTab(self, tab_id) -> bool:
        i = 0
        for j in self.driver.window_handles:
            if j == tab_id:
                self.driver.switch_to.window(self.driver.window_handles[i])
                return True
            i = i + 1
        return False

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

    def navigate(self, url:str):
        self.driver.get(url)

def openProfile(indexProfile, proxy = ''): #proxy: ip:port:username:password or ip:port
    #them cac tham so de khoi tao
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=D:\\MMO\\Gologin\\%s' % indexProfile)
        options.add_argument('--profile-directory=Default')
        options.binary_location = 'D:\\MMO\\Gologin\\orbita-browser\\chrome.exe'
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--no-service-autorun')

        #dung proxy
        if proxy != '':
            infoProxy = proxy.split(':')
            if len(infoProxy) == 4:
                file.changeAuthyProxy(indexProfile, username=infoProxy[2], password=infoProxy[3])
            elif len(infoProxy) == 2:
                file.changeAuthyProxy(indexProfile)
            else: raise Exception
            options.add_argument('--proxy-server=%s' %(infoProxy[0] + ':' + infoProxy[1]))

        #mo profile
        try:
            driver = webdriver.Chrome(driver_executable_path = '.\\chromedriver\\chromedriver.exe', options = options)
        except:
            closeProfile(driver)
        driver.set_page_load_timeout(10)
        return driver
    except: 
        raise Exception


def openTab(driver, url, isFirstTab = False):
    try:
        if isFirstTab == False:
            #driver.tab_new(url)

            driver.execute_script("window.open()")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            time.sleep(0.5)
        else:
            for i in range(0, 3):
                try:
                    driver.get(url)
                    time.sleep(0.5)
                    if driver.current_url == 'chrome://new-tab-page/': 
                        raise Exception
                    break
                except: pass
            if i == 2: raise Exception
    except: raise Exception

def openMultiTab(driver, listUrl):
    try:
        if len(listUrl) > 0:
            openTab(driver, listUrl[0], True)
        j = 1
        while j < len(listUrl):
            openTab(driver, listUrl[j])
            j = j + 1
        driver.switch_to.window(driver.window_handles[0])
        
    except: raise Exception

def closeProfile(driver):
    try:
        while len(driver.window_handles) > 0:
            try:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
            except: pass
    except: pass

    try:
        time.sleep(1)
        driver.quit()
        pass
    except: pass