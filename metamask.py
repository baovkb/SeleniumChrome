import time, goprofile, IOFile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

id = 'cimokgfainmhhjbflkkafbhjancbdimi'
urlMetamask = 'chrome-extension://' + id + '/home.html#'

#This class cointains id of tab which is opening Metamask
class Metamask():
    def __init__(self, gologin): 
        self.tab_id = None

        driver = gologin.driver
        gologin.openTab(urlMetamask)
        if driver.title != 'MetaMask':         
            driver.get('chrome://extensions/')
            # first shadow root, call from driver
            elem1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'extensions-manager')))
            shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", elem1)
            # second shadow_root, call from shadow_root1
            elem2 = shadow_root1.find_element(By.CSS_SELECTOR, 'extensions-item-list[id = "items-list"]')
            shadow_root2 = driver.execute_script("return arguments[0].shadowRoot", elem2)
            # third shadow_root, call from shadow_root2
            #nkbihfbeogaeaoehlefnkodbefgpgknn
            ele = 'extensions-item[id="%s"]' %(id)
            elem3 = shadow_root2.find_element(By.CSS_SELECTOR, ele)
            shadow_root3 = driver.execute_script("return arguments[0].shadowRoot", elem3)
            reload_button = shadow_root3.find_element(By.CSS_SELECTOR, 'cr-button[id="terminated-reload-button"]')
            driver.execute_script("arguments[0].click();", reload_button)
            driver.get(urlMetamask)
        gologin.closeTab()
        
    def openTab(self, gologin):
        gologin.openTab(urlMetamask)
        self.tab_id = gologin.driver.current_window_handle
    
    def closeTab(self, gologin):
        gologin.selectTab(self.tab_id)
        gologin.closeTab()
        self.tab_id = None
    
    def login(self, gologin, password):
        try:
            driver = gologin.driver
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(password)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Unlock"]'))).click()
            try:
                status = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//button[text() = "Assets" or @data-testid="page-container-footer-cancel"]')))
                while status.text == 'Reject':
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="page-container-footer-cancel"]'))).click()
                    status = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text() = "Assets" or @data-testid="page-container-footer-cancel"]')))

            except: pass
            try:
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//button[@class="button btn--rounded btn-primary"]'))).click()
            except: pass
        except: raise ValueError

    def restore(self, gologin, password):
        try:
            driver = gologin.driver
            wait = WebDriverWait(driver, 5)
            info = IOFile.getPhrase(gologin.id)
            seed = info.split(' ')
            driver.get(urlMetamask + 'initialize/create-password/import-with-seed-phrase')
            #wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="MuiInputBase-input MuiInput-input"]'))).send_keys(info)

            lfill = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@class="MuiInputBase-input MuiInput-input"]')))
            for i in range(0, 12):
                lfill[i].send_keys(seed[i])
            lfill[-2].send_keys(password)
            lfill[-1].send_keys(password)

            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="create-new-vault__terms-checkbox"]'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Import"]'))).click()
            WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="All Done"]'))).click()
            time.sleep(1.5)
            pass
        except: raise ValueError

def turnoff(driver):
    goprofile.openTab(driver, 'chrome://extensions/')
    try:
            # first shadow root, call from driver
            elem1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'extensions-manager')))
            shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", elem1)
            # second shadow_root, call from shadow_root1
            elem2 = shadow_root1.find_element(By.CSS_SELECTOR, 'extensions-item-list[id = "items-list"]')
            shadow_root2 = driver.execute_script("return arguments[0].shadowRoot", elem2)
            # third shadow_root, call from shadow_root2
            #nkbihfbeogaeaoehlefnkodbefgpgknn
            elem3 = shadow_root2.find_element(By.CSS_SELECTOR, 'extensions-item[id="nkbihfbeogaeaoehlefnkodbefgpgknn"]')
            shadow_root3 = driver.execute_script("return arguments[0].shadowRoot", elem3)
            reload_button = shadow_root3.find_element(By.CSS_SELECTOR, 'cr-toggle[id="enableToggle"]')
            driver.execute_script("arguments[0].click();", reload_button)
            time.sleep(1)
    except: pass


def importPk(driver, id):
    driver.get(urlMetamask + 'new-account/import')
    pk = IOFile.getPk(id)
    try:
        wait = WebDriverWait(driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="private-key-box"]'))).send_keys(pk)
        WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="No Thanks"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Import"]'))).click()
        time.sleep(1.5)
        pass
    except: raise ValueError

def findNetworkName(driver, profileNetwork):
    try:
        driver.get(urlMetamask + 'settings/networks')
        wait = WebDriverWait(driver, 5)
        listNet = wait.until(EC.presence_of_all_elements_located((By.XPATH, 
        '//div[@class="networks-tab__networks-list-name networks-tab__networks-list-name--disabled" or @class="networks-tab__networks-list-name networks-tab__networks-list-name--selected" or @class="networks-tab__networks-list-name"]')))

        for n in listNet:
            if n.text == profileNetwork['NetworkName']:
                return True
        return False
    except: pass

def addNetwork(driver, profileNetwork):
    try:
        driver.get('http://localhost')
        driver.execute_script('')
        time.sleep(1)
    except: raise ValueError

def addToken(driver, infoToken):
    try:
        driver.get(urlMetamask + 'import-token')
        wait = WebDriverWait(driver, 3)

        #contract
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="custom-address"]'))).send_keys(infoToken['Contract'])
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="custom-symbol"]'))).send_keys(infoToken['Symbol'])
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="custom-decimals"]'))).send_keys(infoToken['Decimal'])
        except: pass
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="page-container-footer-next"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button btn--rounded btn-primary btn--large page-container__footer-button"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="wallet-overview__balance"]')))
    except: pass

def findToken(driver, infoToken):
    try:
        driver.get(urlMetamask)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//li[@data-testid="home__asset-tab"]'))).click()
        time.sleep(2)
        listToken = driver.execute_script('return document.getElementsByClassName("asset-list-item__token-symbol")')
        for l in listToken:
            if l.text == infoToken['Symbol']:
                return True
        return False
    except: pass

def selectNetwork(driver, profileNetwork):
    try:
        driver.get(urlMetamask + 'settings/advanced')
        wait = WebDriverWait(driver, 3)
        checkbox = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]')))
        if checkbox[3].accessible_name == 'OFF':
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/label/div[1]/div[2]/div'))).click()
        
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span'))).click()
        listNet = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="network-name-item"]')))
        for l in listNet:
            if l.text == profileNetwork['NetworkName']: 
                l.click()
                break
    except: pass

def send(driver, profileNetwork, infoToken, receivedAddress):
    if findNetworkName(driver, profileNetwork) == False:
        addNetwork(driver, profileNetwork)

    selectNetwork(driver, profileNetwork)
    if findToken(driver, infoToken) == False:
        addToken(driver, infoToken)
    try:
        driver.get(urlMetamask + 'send')
        wait = WebDriverWait(driver, 7)
    
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ens-input__wrapper__input'))).send_keys(receivedAddress)

        #select token
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'send-v2__asset-dropdown__asset'))).click()
        listToken = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="token-list-item__symbol" or @class="send-v2__asset-dropdown__symbol"]')))
        for l in listToken:
            if l.text == infoToken['Symbol']:
                l.click()
                break
        #input amount
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="unit-input__input"]'))).send_keys('0')
        #next button
        next = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button btn--rounded btn-primary page-container__footer-button"]')))
        driver.execute_script("arguments[0].click();", next)
        #confirm button

        confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button btn--rounded btn-primary page-container__footer-button"]')))
        driver.execute_script("arguments[0].click();", confirm)
        time.sleep(5)
        
    except: pass




    
