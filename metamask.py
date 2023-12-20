import time, goprofile, IOFile

import undetected_chromedriver as webdriver
from tabs import Tabs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

id = 'cimokgfainmhhjbflkkafbhjancbdimi'
urlMetamask = 'chrome-extension://' + id + '/home.html#'

class Metamask(Tabs):
    def __init__(self, driver: webdriver): 
        super().__init__()
        # super().openTab(driver, urlMetamask)
        # if driver.title != 'MetaMask':         
        #     driver.get('chrome://extensions/')
        #     # first shadow root, call from driver
        #     elem1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'extensions-manager')))
        #     shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", elem1)
        #     # second shadow_root, call from shadow_root1
        #     elem2 = shadow_root1.find_element(By.CSS_SELECTOR, 'extensions-item-list[id = "items-list"]')
        #     shadow_root2 = driver.execute_script("return arguments[0].shadowRoot", elem2)
        #     # third shadow_root, call from shadow_root2
        #     #nkbihfbeogaeaoehlefnkodbefgpgknn
        #     ele = 'extensions-item[id="%s"]' %(id)
        #     elem3 = shadow_root2.find_element(By.CSS_SELECTOR, ele)
        #     shadow_root3 = driver.execute_script("return arguments[0].shadowRoot", elem3)
        #     reload_button = shadow_root3.find_element(By.CSS_SELECTOR, 'cr-button[id="terminated-reload-button"]')
        #     driver.execute_script("arguments[0].click();", reload_button)
        #     driver.get(urlMetamask)
        # super().closeTab(driver)
        
    def openTab(self, driver: webdriver):
        super().openTab(driver, urlMetamask)
        
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