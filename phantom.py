import os
import IOFile as file
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import profile, time, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

def init(driver, url):
    profile.openTab(driver, url)

def destruct(driver):
    try:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except: 
        try:
            driver.switch_to.window(driver.window_handles[0])
        except: raise Exception

def phantom(driver, index):
    init(driver, 'chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/onboarding.html')

    try:
        phrase = file.getPhrase(index)
        phrase = phrase.split(' ')
        
        script = 'document.getElementsByClassName("sc-bdvvtL ljDDId")[0].click()'
        driver.execute_script(script)

        input = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@class="sc-AjmGg fhSPvt"]')))

        j = 0
        for i in input:
            i.send_keys(phrase[j])
            j = j + 1

        #submit
        script = 'document.getElementsByClassName("sc-bdvvtL jdiDvS")[0].click()'
        driver.execute_script(script)

        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="sc-bdvvtL jdiDvS"]'))).click()

        #password
        input = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@class="sc-bBHxTw bkoEtZ"]')))
        for i in input:
            i.send_keys('bao21022002')

        driver.find_element(By.XPATH, '//*[@id="root"]/main/div[2]/form/div[2]/span/input').click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="sc-bdvvtL jdiDvS"]'))).click()
        time.sleep(1.5)

    except: raise ValueError

def getPrivate(driver):
    init(driver, 'chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/popup.html')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="unlock-form-password-input"]'))).send_keys('bao21022002')
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="sc-bdvvtL jdiDvS"]'))).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/section/div[1]/p'))).click()
        time.sleep(0.2)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[5]/div/div/div[1]/div[4]'))).click()
        time.sleep(0.2)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[5]/div/div/div/div[4]/div[1]'))).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys('bao21022002')
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="primary-button"]'))).click()
        time.sleep(0.2)
        pri = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//textarea[@class="sc-fbyfCU sc-GEbAx sc-jlsrNB eKookP hRzVdO bHCmnc"]')))
        # add = getClipboard()
        with open("D:\\MMO\\wallet\\sol_privatekey.txt", mode='a', encoding='utf-8') as out:
            out.write(pri.text + '\n')
    except: 
        input('Loi')