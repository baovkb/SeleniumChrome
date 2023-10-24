import code
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import IOFile as file
import random, time, pf


def init(driver):
    pf.openTab(driver, 'https://mail.google.com/mail/u/0/h/1imt096xqt7k2')
    try:
        WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maia-main"]/form/p/input'))).click()
    except: pass

def readMail(driver):
    init(driver)
    try:
        for i in range(0, 3):
            listMail = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="ts"]')))
            codeConfirm = ''
            for mail in listMail:
                if mail.text.find('Welcome to Aptos Community') != -1:
                    # codeConfirm = mail.text.replace('Your verification code - Your confirmation code is', '')
                    # codeConfirm = codeConfirm.replace(' ', '')
                    mail.click()
                    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[4]/td/div/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table[6]/tbody/tr/td/table/tbody/tr/td/a'))).click()
                    break
            # if codeConfirm == '':
            #     time.sleep(2)
            #     driver.refresh()
            #     continue
            time.sleep(1)
            destruct(driver)
            return codeConfirm
    except: pass

def destruct(driver):
    try:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except: 
        try:
            driver.switch_to.window(driver.window_handles[0])
        except: raise Exception
