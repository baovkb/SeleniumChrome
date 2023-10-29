from calendar import WEDNESDAY
from cmath import phase
from lib2to3.pgen2.driver import Driver
import os
from tkinter import E, W
import weakref
import IOFile as file
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import goprofile, time, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import metamask as meta
import mail

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

def fusionist(driver):
    init(driver, 'https://ace.fusionist.io/account/endurance')
    wait = WebDriverWait(driver, 3)
    curtab = driver.current_window_handle
    #change net
    try:
        # driver.execute_script('''ethereum.request({ method: 'eth_requestAccounts' });''')
        # time.sleep(1.2)
        # driver.switch_to.window(driver.window_handles[1])
        # driver.get('chrome-extension://cogfooeaiphfblbojceehjkhifalpbml/home.html#')
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Next"]'))).click()
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Connect"]'))).click()
        # driver.switch_to.window(curtab)
        time.sleep(2)
        driver.execute_script('''
        window.ethereum.request({
            method: "wallet_addEthereumChain",
            params: [{
                chainId: "0x288",
                rpcUrls: ["https://rpc-endurance.fusionist.io"],
                chainName: "Endurance",
                nativeCurrency: {
                name: "ACE",
                symbol: "ACE",
                decimals: 18
                },
                blockExplorerUrls: ["https://explorer-endurance.fusionist.io"]
            }]
            });
        '''
        )
        time.sleep(1.2)
        driver.switch_to.window(driver.window_handles[1])
        driver.get('chrome-extension://cogfooeaiphfblbojceehjkhifalpbml/home.html#')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button btn--rounded btn-primary"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button btn--rounded btn-primary"]'))).click()
    except: pass
    driver.switch_to.window(curtab)

    try:
        #claim faucet
        try:
            button =  WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Connect Wallet"]')))
            try:
                driver.execute_script("arguments[0].click();", button)
                time.sleep(1)
                #WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Connect Wallet"]'))).click()
                WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="MetaMask"]'))).click()
                try:
                    time.sleep(1.2)
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get('chrome-extension://cogfooeaiphfblbojceehjkhifalpbml/home.html#')
                    WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="request-signature__sign"]'))).click()
                    time.sleep(0.5)
                except:
                    pass
                finally: driver.switch_to.window(curtab)
                driver.get('https://ace.fusionist.io/account/endurance')
            except: pass

            try:
                button1 = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div[3]/div/div[1]/div/div/div[5]/button')))
                if button1.text == 'Claim':
                    button1.click()
                    time.sleep(1.2)
            except: pass
            
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[3]/div[3]/div/div[2]/div/div/div[5]/div[1]/button'))).click()
            time.sleep(1.2)
            driver.switch_to.window(driver.window_handles[1])
            driver.get('chrome-extension://cogfooeaiphfblbojceehjkhifalpbml/home.html#')
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="page-container-footer-next"]'))).click()
            except: raise ValueError
            time.sleep(1.5)
        except: pass
    except ValueError: raise ValueError
    except: pass

def quizZeta(driver, id):
    init(driver, 'https://docs.google.com/forms/d/e/1FAIpQLSd_cVX_CArycdutWIL70jQZPtPt3kdNtjYw8iDP8khKXivNAg/viewform')

    try:
        info = file.getInfoProfile(id)
        wait = WebDriverWait(driver, 5)
        time.sleep(2)
        add = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        add.clear()
        add.click()
        add.send_keys(info['evm'])
        time.sleep(1.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'))).click() #4
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'))).click() #1
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'))).click() #3
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'))).click() #4
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'))).click() #1
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'))).click() #2
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'))).click() #4

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'))).click()

        for j in range(0,3):
            if driver.current_url.find('formResponse'):
                break

            time.sleep(1)

    except: raise ValueError

def youtube(driver, url):
    init(driver, url)

    try:
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button'))).click()
        time.sleep(1.5)
    except: pass


def pontem_extension(driver, index, url = 'chrome-extension://embmdnkpiegkicljkhnmoifnjkcfhjch/index.html#'):
    init(driver, url)

    try:
        phrase = file.getPhrase(index)
        phrase = phrase.split(' ')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pitaka"]/div/div/div/div[1]/a[2]/div[2]/div[2]'))).click()
        fill = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="password"]')))

        i = 0
        for ph in fill:
            if i >= 12:
                break
            ph.send_keys(phrase[i])
            i = i + 1

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('bao21022002')
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirm"]'))).send_keys('bao21022002')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/main/form/button'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pitaka"]/div/div/div/div[2]/button')))
    except: raise ValueError


def polkadot(driver, index):
    init(driver, 'chrome-extension://mbhdmihlloeodgpdhmakmcbiobcejdkh/index.html#/account/import-seed')

    phrase = file.getPhrase(index)
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[3]/div[1]/textarea'))).send_keys(phrase)
        #next
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="Button-sc-1gyneog-0 eZHvKI NextStepButton-sc-26dpu8-0 jyABgM"]'))).click()
        #name
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[3]/div/input'))).send_keys(str(index).zfill(3))
        #password
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[4]/div/input'))).send_keys('bao21022002')
        #password again
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div[5]/div[1]/input'))).send_keys('bao21022002')
        #add
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="Button-sc-1gyneog-0 eZHvKI NextStepButton-sc-26dpu8-0 jyABgM"]'))).click()
        #confirm understood
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="Button-sc-1gyneog-0 eZHvKI"]'))).click()
        time.sleep(1.5)
    except: ValueError

def petra(driver, index):
    init(driver, 'chrome-extension://lkkkkocnnkkdcdondchcfbjdmfkifmdk/index.html')

    phrase = file.getPhrase(index)
    phrase = phrase.split(' ')

    #import wallet click
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="chakra-button css-t5mrhf"]'))).click()
    #input password
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div[1]/div/input'))).send_keys('bao21022002')
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div[2]/div/input'))).send_keys('bao21022002')
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/label/span[1]'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/button[2]'))).click()
    #import mnemonic
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/form/div/button[2]'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/button[2]'))).click()

    fill = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@class="chakra-input css-imfiyd"]')))
    for f, p in zip(fill, phrase):
        f.send_keys(p)
    time.sleep(0.2)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/button[2]'))).click()
    time.sleep(1.5)

def fuel_wallet(driver, index):
    init(driver, 'chrome-extension://mlnfibpcjolbchnackmchbpfepfnidni/index.html#/sign-up/welcome')

    phrase = file.getPhrase(index)
    phrase = phrase.split(' ')
    wait = WebDriverWait(driver, 5)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div/div[2]/button[2]'))).click()

    field = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@aria-label="Type your text"]')))

    i = 0
    for j in field:
        j.send_keys(phrase[i])
        i = i + 1

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div[2]/div[4]/button[2]'))).click()

def joinTele(driver, urlChannel, urlGroup):
    try:
        init(driver, urlChannel)
    except:
        driver.close()
        init(driver, urlChannel)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'chat-utils')))
        while True:
            try:
                join_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn-primary btn-color-primary chat-join rp"]')))
                driver.execute_script("arguments[0].click();", join_button)
                time.sleep(1)
            except: 
                break
        
        driver.get(urlGroup)
        while True:
            try:
                join_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn-primary btn-color-primary chat-join rp"]')))
                driver.execute_script("arguments[0].click();", join_button)
                time.sleep(1)
            except: 
                break
        
        # time.sleep(2)
        # proveHuman = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="reply-markup-button rp tgico"]')))
        # for p in proveHuman:
        #     if p.accessible_name == "Click here to prove you're human":
        #         driver.execute_script("arguments[0].click();", p)
        #     try:
        #         WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'input-message-input i18n scrollable scrollable-y no-scrollbar')))
        #         break
        #     except: pass
            

    except: raise ValueError

def arco_protocol(driver, url):
    init(driver, url)

    try:
        wait = WebDriverWait(driver, 7)
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys('bao21022002')
        unlock_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Unlock"]')))
        driver.execute_script('arguments[0].click()', unlock_button)
        time.sleep(1)
        
        #switch to testnet
        numTab = driver.window_handles
        curr_tab = driver.current_window_handle

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]'))).click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[2]'))).click()
        time.sleep(1)
        driver.execute_script("for (var i = 0; i < 5; ++i) document.getElementsByClassName('sc-kDvujY tjfuV')[0].click()")
        time.sleep(2)

        driver.get('https://arcoprotocol.tech/')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/button'))).click()
        time.sleep(0.2)
        driver.execute_script("document.getElementsByClassName('MuiBox-root css-1jnapd8')[0].click()")
        
        try:
            WebDriverWait(driver, 4).until(EC.new_window_is_opened(numTab))
            driver.switch_to.window(driver.window_handles[-1])
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
        except: pass

        driver.switch_to.window(curr_tab)
        
        #deposit
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[5]/button[1]'))).click()
        #pop up transaction
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="MuiBox-root css-4juldg"]')))
        #input amount
        num = random.uniform(2, 3)
        num = round(num, 1)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r0:"]'))).send_keys(num)
        wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-bo865z"]'))).click()
        wait.until(EC.new_window_is_opened(numTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
        driver.switch_to.window(curr_tab)

        while True:
            try:
                driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-4juldg"]')
                driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-4juldg > div.MuiBox-root.css-1ghqxvq > svg').click()
            except: break

        time.sleep(4)
        #borrow
        bo = round(random.uniform(0.05, 0.2), 2)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[5]/button[2]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r1:"]'))).send_keys(bo)
        wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-bo865z"]'))).click()
        wait.until(EC.new_window_is_opened(numTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
        driver.switch_to.window(curr_tab)

        while True:
            try:
                driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-4juldg"]')
                driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-4juldg > div.MuiBox-root.css-1ghqxvq > svg').click()
            except: break

        time.sleep(4)
        #withdraw
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[5]/button[1]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r2:"]'))).send_keys(round(random.uniform(0.05, 0.2), 2))
        wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-bo865z"]'))).click()
        wait.until(EC.new_window_is_opened(numTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
        driver.switch_to.window(curr_tab)

        while True:
            try:
                driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-4juldg"]')
                driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-4juldg > div.MuiBox-root.css-1ghqxvq > svg').click()
            except: break


        time.sleep(4)
        #repay
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[5]/button[2]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r3:"]'))).send_keys(round(bo - 0.02, 2))
        wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-bo865z"]'))).click()
        wait.until(EC.new_window_is_opened(numTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
        driver.switch_to.window(curr_tab)
        while True:
            try:
                driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-4juldg"]')
                driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-4juldg > div.MuiBox-root.css-1ghqxvq > svg').click()
            except: break

        time.sleep(3)

    except: raise ValueError

def martianMintNft(driver, url, index, password = 'bao21022002'):
    init(driver, url)

    try:
        numTab = driver.window_handles
        curr_tab = driver.current_window_handle
        wait = WebDriverWait(driver, 7)
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(password)
        unlock_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Unlock"]')))
        driver.execute_script('arguments[0].click()', unlock_button)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[6]/div[1]/div[2]'))).click()
        time.sleep(1.5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[6]/div[1]/div[3]/div/div/div[2]/div/p'))).click()

        #connect tw
        wait.until(EC.new_window_is_opened(numTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="allow"]'))).click()
        time.sleep(1.5)
    except: pass

    #     #switch to testnet
    #     numTab = driver.window_handles
    #     curr_tab = driver.current_window_handle

    #     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]'))).click()
    #     time.sleep(1)
    #     wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/div'))).click()
    #     driver.execute_script("document.getElementsByClassName('sc-ipEyDJ hzcrTR')[1].click()")
    #     wait.until(EC.new_window_is_opened(numTab))
    #     driver.switch_to.window(driver.window_handles[-1])
        
    #     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="new_wallet"]/ol/li[1]/button'))).click()
    #     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_dialog"]/div/div[3]/form[1]/button'))).click()
    #     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/button[2]/div'))).click()

    #     Info = file.getInfoProfile(index)
    #     try:
    #         wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Create username"]'))).send_keys(Info['username'])
    #         wait.until(EC.presence_of_element_located((By.ID, 'user_terms_accepted'))).click()
    #         time.sleep(1)
    #         wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div[2]/div/form/div[4]/button'))).click()
    #         wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div/div[2]/div/p[1]')))
            
    #         #confirm mail
    #         time.sleep(3)
    #         mail.readMail(driver)
    #         WebDriverWait(driver, 3.5).until(EC.presence_of_element_located((By.LINK_TEXT, 'VERIFY EMAIL'))).click()
    #         wait.until(EC.new_window_is_opened(numTab))
    #         driver.switch_to.window(driver.window_handles[-1])
    #         while driver.current_url.find('https://aptoslabs.com/settings/profile') == -1: pass
    #         time.sleep(0.5)
    #         driver.get('https://aptoslabs.com/testnet-faucet')
    #         curr_tab = driver.current_window_handle
    #         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="new_wallet"]/ol/li[2]/div[2]/button'))).click()
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-wallet="martian"]'))).click()

    #         wait.until(EC.new_window_is_opened(numTab))
    #         driver.switch_to.window(driver.window_handles[-1])
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
    #         time.sleep(1)
    #         wait.until(EC.new_window_is_opened(numTab))
    #         driver.switch_to.window(driver.window_handles[-1])
    #         WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()

    #         driver.switch_to.window(curr_tab)
    #         time.sleep(4)
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-use-faucet-target="button"]'))).click()
    #         time.sleep(0.5)
    #         driver.switch_to.window(driver.window_handles[0])
    #         driver.refresh()
    #         numTab = driver.window_handles
    #         time.sleep(1)
    #         wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Connect Martian"]')))
    #         driver.execute_script("document.getElementsByClassName('sc-htpNat hYwuAf')[0].click()")

    #         wait.until(EC.new_window_is_opened(numTab))
    #         driver.switch_to.window(driver.window_handles[-1])
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
    #         driver.switch_to.window(driver.window_handles[0])
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/button'))).click()

    #         wait.until(EC.new_window_is_opened(numTab))
    #         driver.switch_to.window(driver.window_handles[-1])
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
    #         try:
    #             wait.until_not(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button')))
    #         except: pass

    #         WebDriverWait(driver, 10).until(EC.new_window_is_opened(numTab))
    #         driver.switch_to.window(driver.window_handles[-1])
    #         WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[5]/button'))).click()
    #         wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[text()="NFT Mint Success"]')))

    #     except: pass
    # except: raise Exception


def zeta(driver, url):
    init(driver, url)
    try:
        curTab = driver.current_window_handle
        numTab = len(driver.window_handles)
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/button'))).click()
        except: pass

        #try:
            #connect tw
        #     try:
        #         WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div[1]/div/div[2]/button'))).click()
        #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/span/span'))).click()
        #         WebDriverWait(driver, 3).until(EC.url_to_be('https://labs.zetachain.com/leaderboard'))
        #     except: pass
            
        #     #connect meta
        # for j in range(0, 2):
        #     try:
        #         try:
        #             WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div[1]/div/div[3]/div/button'))).click()
        #         except: break
        #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/button/div/div/div[1]'))).click()
        #         time.sleep(1)
        #         if len(driver.window_handles) > numTab:
        #             driver.switch_to.window(driver.window_handles[-1])
        #         else:
        #             profile.openTab(driver, 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        #             driver.switch_to.window(driver.window_handles[-1])
                
        #         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]'))).click()
        #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()

        #         #confirm network
        #         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]'))).click()
        #         if len(driver.window_handles) > numTab:
        #             driver.close()
        #         driver.switch_to.window(curTab)
        #         break
        #     except: pass
            
        #     try:
        #         #confirm wallet
        #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div[1]/div/button'))).click()
        #         time.sleep(1)
        #         if len(driver.window_handles) > numTab:
        #             driver.switch_to.window(driver.window_handles[-1])
        #         else:
        #             profile.openTab(driver, 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        #             driver.switch_to.window(driver.window_handles[-1])
        #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[4]/button[2]'))).click()
        #         time.sleep(1)
        #         if len(driver.window_handles) > numTab:
        #             driver.close()
        #         driver.switch_to.window(curTab)

        #         time.sleep(2)
        #     except: pass
        # except: pass

        # #change network
        # whatnet = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/header/div/div/div[2]/div/div[2]/button[1]/span/img')))
        # if whatnet.accessible_name != 'Polygon Mumbai':
        #     for t in range(0, 2):
        #         try:
        #             button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textInfo MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root e1hxx02w0 e3n5t3y0 css-epyu23"]')))
        #             driver.execute_script("arguments[0].click();", button)
        #             net = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="iekbcc0 iekbcc9 ju367vo ju367va"]')))
        #             driver.execute_script("arguments[0].click();", net[2])
        #             time.sleep(1)
        #             if len(driver.window_handles) > numTab:
        #                 driver.switch_to.window(driver.window_handles[-1])
        #             else:
        #                 profile.openTab(driver, 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
        #                 driver.switch_to.window(driver.window_handles[-1])
        #             WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="button btn--rounded btn-primary"]'))).click()
        #         except: pass
        #         if len(driver.window_handles) > numTab:
        #             driver.close()
        #         driver.switch_to.window(curTab)
        #         whatnet = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/header/div/div/div[2]/div/div[2]/button[1]/span/img')))
        #         if whatnet.accessible_name == 'Polygon Mumbai':
        #             break

        #     time.sleep(3)

        #  #get asset
        # try:
        #     driver.get('https://labs.zetachain.com/get-zeta')
        #     time.sleep(2)
        #     button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root e3n5t3y0 css-grl2qq"]')))
        #     driver.execute_script("arguments[0].click();", button)
        #     try: time.sleep(2)
        #     #   WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/main/div/div[1]/a[1]/button')))
        #     except: pass
        # except: pass
        
        driver.get('https://labs.zetachain.com/swap')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/div[2]/div[1]/div[2]/div/button[1]'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/button[3]'))).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/div[2]/div[1]/div[2]/div/button[2]'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/button[2]'))).click()

        #select network 2
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/div[2]/div[3]/div[2]/div/button[1]'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/button'))).click()

        #select token 2
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/div[2]/div[3]/div[2]/div/button[2]'))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/button[1]'))).click()

        #change
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/div[2]/div[2]/button/div[1]'))).click()

        #input amount
        rd = random.uniform(2, 2.5)
        rd = round(rd, 3)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/div[2]/div[1]/div[2]/input'))).send_keys(rd)
        
        #review order
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root e3n5t3y0 css-grl2qq"]')))
        driver.execute_script("arguments[0].click();", button)

        #approve
        try:
            button = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/main/div/div/div/div/button[1]')))
            driver.execute_script("arguments[0].click();", button)
            time.sleep(5)
            if len(driver.window_handles) > numTab:
                driver.switch_to.window(driver.window_handles[-1])
            else:
                goprofile.openTab(driver, 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
                driver.switch_to.window(driver.window_handles[-1])
            approve = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//button[@data-testid="page-container-footer-next"]')))
            driver.execute_script("arguments[0].click();", approve)
            driver.switch_to.window(curTab)
        except: pass

        #swap button
        button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButtonBase-root e3n5t3y0 css-grl2qq"]')))
        driver.execute_script("arguments[0].click();", button)

        time.sleep(5)
        if len(driver.window_handles) > numTab:
            driver.switch_to.window(driver.window_handles[-1])
        else:
            goprofile.openTab(driver, 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
            driver.switch_to.window(driver.window_handles[-1])
        swap = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="page-container-footer-next"]')))
        driver.execute_script("arguments[0].click();", swap)
        driver.switch_to.window(curTab)

        try:
            time.sleep(1)
            p = driver.find_element(By.XPATH, '//div[@class="cursor-pointer hover:bg-grey-500 whitespace-nowrap flex items-center flex-grow-0 css-1jv8mrw eqz6u830"]').text
            while driver.find_element(By.XPATH, '//div[@class="cursor-pointer hover:bg-grey-500 whitespace-nowrap flex items-center flex-grow-0 css-1jv8mrw eqz6u830"]').text == p: pass
        except: pass
    except: 
        raise ValueError


def getFaucet(driver, url, index):
    init(driver, url)
    Info = file.getInfoProfile(index)
    
    for i in range(0, 3):
        try:
            while True:
                try:
                    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Input your Binance Smart Chain address..."]')))
                    #driver.find_element(By.XPATH, '//input[@placeholder="Input your Binance Smart Chain address..."]')
                    break
                except: pass

            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="url"]'))).send_keys(Info['evm'])
            time.sleep(0.3)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contendBody"]/div/div[2]/div/div/span[2]/button'))).click()
            time.sleep(0.3)
            driver.find_element(By.XPATH, '//*[@id="contendBody"]/div/div[2]/div/div/span[2]/ul/li[6]/a').click()
            #menu.select_by_value('0.5 BNBs')
            time.sleep(1)
            break
        except: driver.get(url)

def knok(driver, url, index):
    init(driver, url)

    try:
        numTab = driver.window_handles
        curr_tab = driver.current_window_handle

        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div[2]/div/div[1]'))).click()

        wait.until(EC.new_window_is_opened(numTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="field-:r1:"]'))).send_keys('bao21022002')
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="prompt"]/div/form/div/div[2]/button'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="prompt"]/div/div[3]/button[2]'))).click()
        driver.switch_to.window(curr_tab)

        Info = file.getInfoProfile(index)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-perfect"]/div[2]/div[1]/input'))).send_keys(Info['username'])
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-perfect"]/div[2]/div[2]/div[1]/span'))).click()

        year = str(random.randint(1980, 2004))
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 28)).zfill(2)

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-perfect"]/div[2]/div[3]/input'))).send_keys(year + month + day)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-perfect"]/div[2]/div[4]'))).click()

        #invite code
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-invite"]/div[2]/div[1]/input'))).send_keys('7VG2')
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-invite"]/div[2]/div[3]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="chat"]/div[1]/div/div/span')))
        time.sleep(1)

    except: raise ValueError

def martian(driver, index):
    init(driver, 'chrome-extension://eciknjminelacimnecbheohohjljpjgh/onboarding/onboarding.html')

    try:
        wait = WebDriverWait(driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div/div[4]/div'))).click()
        time.sleep(1)
        driver.execute_script("document.getElementsByClassName('sc-gswNZR gVwxSb')[0].click()")

        phrase = file.getPhrase(index)
        phrase = phrase.split(' ')
        field_phrase = driver.execute_script("return document.getElementsByClassName('MuiInputBase-input css-mnn31')")

        k = 0
        for i in field_phrase:
            i.send_keys(phrase[k])
            k = k + 1

        driver.execute_script("document.getElementsByClassName('sc-dkrFOg FdmMC')[0].click()")
        time.sleep(1)

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div/div[3]/div/div[2]/div/input'))).send_keys('bao21022002')
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/main/div/div[4]/div/div[2]/div/input'))).send_keys('bao21022002')
        driver.execute_script("document.getElementsByClassName('PrivateSwitchBase-input css-1m9pwf3')[0].click()")
        driver.execute_script("document.getElementsByClassName('sc-dkrFOg kmtnUS')[0].click()")
        for j in range(0, 3):
            time.sleep(0.2)
            driver.execute_script("document.getElementsByClassName('sc-dkrFOg FdmMC')[0].click()")
    except: raise Exception

def loginPontem(driver, password):
    init(driver, 'chrome-extension://embmdnkpiegkicljkhnmoifnjkcfhjch/index.html#/auth/unlock?r=/')

    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(password)
        unlock_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Unlock"]')))
        driver.execute_script('arguments[0].click()', unlock_button)
        try:
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/button'))).click()
        except: pass
        time.sleep(1)
        #switch to devnet
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/div[1]/header/div/button[1]'))).click()
        time.sleep(0.5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="network-menu"]/div[3]/ul/div[2]/li[3]/div[2]/span/div'))).click()
        #get faucet
        for i in range(0, 4):
            time.sleep(0.5)
            driver.execute_script("document.getElementsByClassName('AccountInfo_actionIcon__G0+Ak')[1].click()")
    except: raise Exception

def atodex(driver):
    init(driver, 'https://devnet.atodex.io/swap/')
    curTab = driver.current_window_handle

    try:
        # #connect wallet
        wait = WebDriverWait(driver, 7)
        for i in range(0,2):
            time.sleep(1.2)
            driver.switch_to.window(driver.window_handles[1])
            try:
                WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/div/div/section/div/button[2]'))).click()
                time.sleep(0.5)
                try:
                    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/div/div/section/div/button[2]'))).click()
                except: pass
                break
            except:
                driver.switch_to.window(curTab)
                driver.execute_script("document.getElementsByClassName('sc-af1f6b81-0 evgOwa')[0].click()")
                time.sleep(0.3)
                wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/reach-portal[2]/div[2]/div/div/div/div[2]/div[3]'))).click()
        driver.switch_to.window(curTab)
        time.sleep(1)
        listTab = driver.window_handles

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[5]/div[1]/div[1]'))).click()
        time.sleep(0.3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="tADX"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/input'))).send_keys('1')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[6]/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/reach-portal/div[2]/div/div/div/div[2]/button'))).click()

        wait.until(EC.new_window_is_opened(listTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/div/div[1]/footer/div/div[2]/button'))).click()
        driver.switch_to.window(curTab)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Transaction Submitted"]')))
        driver.refresh()

        #swap tADX-USDT
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div[1]'))).click()
        time.sleep(0.3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="tADX"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[5]/div[1]/div[1]'))).click()
        time.sleep(0.3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="USDT"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[3]/button[1]'))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[6]/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/reach-portal/div[2]/div/div/div/div[2]/button'))).click()
        wait.until(EC.new_window_is_opened(listTab))
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/div/div[1]/footer/div/div[2]/button'))).click()
        driver.switch_to.window(curTab)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Transaction Submitted"]')))

        try:
            driver.get('https://devnet.atodex.io/add-liquidity/new/')
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[5]/div[1]/div[1]'))).click()
            time.sleep(0.3)
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="tADX"]'))).click()
            num = random.uniform(0.1, 0.2)
            num = round(num, 3)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[2]/div[2]/input'))).send_keys(num)

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/div[6]/button'))).click()
            time.sleep(1.7)
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/reach-portal/div[2]/div/div/div/div[2]/button'))).click()
            wait.until(EC.new_window_is_opened(listTab))
            driver.switch_to.window(driver.window_handles[-1])
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/div/div[1]/footer/div/div[2]/button'))).click()
            driver.switch_to.window(curTab)
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Transaction Submitted"]')))
        except: pass

        try:
            driver.get('https://devnet.atodex.io/faucet/')
            wait.until_not(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div/button')))
            
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[3]/div/div[2]/button'))).click()
            wait.until(EC.new_window_is_opened(listTab))
            driver.switch_to.window(driver.window_handles[-1])
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pitaka"]/div/div/div/div[1]/footer/div/div[2]/button'))).click()
            driver.switch_to.window(curTab)
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Transaction Submitted"]')))
        except: pass

        driver.get('https://devnet.atodex.io/mission/')
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[3]/div/button')))
        for i in range(0, 6):
            try:
                driver.execute_script("document.getElementsByClassName('sc-af1f6b81-0 eEZwyW btn-claim')[0].click()")
                time.sleep(0.3)
            except: pass
            try:
                driver.execute_script("document.getElementsByClassName('sc-af1f6b81-0 eEZwyW btn-claim')[1].click()")
                time.sleep(0.4)
            except: pass
            try:
                driver.execute_script("document.getElementsByClassName('sc-af1f6b81-0 eEZwyW btn-claim')[2].click()")
                time.sleep(0.3)
            except: pass
        try:
            driver.execute_script("document.getElementsByClassName('sc-af1f6b81-0 eEZwyW btn-claim')[2].click()")
            driver.execute_script("document.getElementsByClassName('sc-af1f6b81-0 eEZwyW btn-claim')[2].click()")
            time.sleep(0.3)
        except: pass
    except: raise ValueError