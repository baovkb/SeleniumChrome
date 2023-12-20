import os
import IOFile as file
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import goprofile, time, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import metamask as meta

def init(driver, url):
    goprofile.openTab(driver, url)

def destruct(driver):
    try:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except: 
        try:
            driver.switch_to.window(driver.window_handles[0])
        except: raise Exception

def form(driver, url):
    init(driver, url)

    i = 1
    Info = file.readFile("D:\\MMO\\Tool\\Manage_Profile_Gologin\\data\\address.txt", i)
    while Info != '':
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(Info)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'))).click()
        time.sleep(1)
        driver.get(url)
        Info = file.readFile("D:\\MMO\\Tool\\Manage_Profile_Gologin\\data\\address.txt", i)
        i = i + 1


def ggForm(driver, url, indexProfile, dicXpath, linkQuoteTw = ''):
    init(driver, url)
    if (driver.current_url).find('alreadyresponded') != -1:
        return
    Info = file.getInfoProfile(indexProfile)
    try: 
        time.sleep(1.5)
        wait = WebDriverWait(driver, 5)
        if dicXpath['email'] != '':
            email = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['email'])))
            email.clear()
            email.send_keys(Info['email'])
            time.sleep(0.3)
        if dicXpath['usenameTele'] != '':
            userTele = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['usenameTele'])))
            userTele.clear()
            userTele.send_keys(Info['userTelegram'])
            time.sleep(0.3)
        if dicXpath['linkTele'] != '':
            linkTele = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['linkTele'])))
            linkTele.clear()
            linkTele.send_keys(Info['linkTelegram'])
            time.sleep(0.3)
        if dicXpath['usernameTw'] != '':
            userTw = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['usernameTw'])))
            userTw.clear()
            userTw.send_keys(Info['userTwitter'])
            time.sleep(0.3)
        if dicXpath['linkTw'] != '':
            linkTw = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['linkTw'])))
            linkTw.clear()
            linkTw.send_keys(Info['linkTwitter'])
            time.sleep(0.3)
        if dicXpath['usernameDiscord'] != '':
            userDis = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['usernameDiscord'])))
            userDis.clear()
            userDis.send_keys(Info['userDiscord@'])
            time.sleep(0.3)
        if dicXpath['usernameDiscordWith#'] != '':
            userDisS = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['usernameDiscordWith#'])))
            userDisS.clear()
            userDisS.send_keys(Info['userDiscord'])
            time.sleep(0.3)
        if dicXpath['metamaskAddress'] != '':
            meta = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['metamaskAddress'])))
            meta.clear()
            meta.send_keys(Info['evm'])
            time.sleep(0.3)
        if dicXpath['solanaAddress'] != '':
            sol = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['solanaAddress'])))
            sol.clear()
            sol.send_keys(Info['sol'])
            time.sleep(0.3)

        if dicXpath['linkQuoteTw'] != '':
            linkQTw = wait.until(EC.presence_of_element_located((By.XPATH, dicXpath['linkQuoteTw'])))
            linkQTw.clear()
            linkQTw.send_keys(linkQuoteTw)
            time.sleep(0.3)

        # add = file.readAddress(indexProfile)
        # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i21"]/div[3]/div'))).click()
        
        # user = Info['userDiscord'].split('#')
        # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(user[0])

        #attachment
        # driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/span/span[2]').click()
        # time.sleep(2)
        # iframe = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'iframe')))
        # while len(iframe) <= 1:
        #     iframe = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'iframe')))
        # driver.switch_to.frame(iframe[1])
        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":g.select-files-button"]/div'))).click()
        # time.sleep(1)

        # try:
        #     import autoit
        #     autoit.win_activate('Open')
        #     autoit.control_send("Open","Edit1",r"C:\Users\my computer\Documents\vote.jpg")
        #     time.sleep(0.5)
        #     autoit.control_send("Open","Edit1","{ENTER}")
        #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="picker:ap:0"]'))).click()

        # except: raise ValueError

        # driver.switch_to.default_content()
        # WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//div[text() = "vote.jpg"]')))

        # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="i25"]/div[3]/div'))).click()

        WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'))).click()
        for j in range(0,3):
            if driver.current_url.find('formResponse'):
                break

            time.sleep(1)
    except: 
        raise ValueError
    destruct(driver)


