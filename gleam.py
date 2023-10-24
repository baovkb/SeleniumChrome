from selenium.webdriver.common.action_chains import ActionChains
import profile, time, IOFile as file
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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

def loginGleamWithTwitter(driver, index):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.twitter-background.popup-window')))
    window_gl = driver.current_window_handle
    numTab = driver.window_handles
    driver.execute_script("document.getElementsByClassName('twitter-background popup-window')[0].click()")
    wait.until(EC.new_window_is_opened(numTab))

    try:
        window_tw = driver.window_handles[-1]
        driver.switch_to.window(window_tw)
        #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'submit button selected')))
        driver.execute_script("document.getElementsByClassName('submit button selected')[0].click()")
    except: 
        pass
    finally:
        driver.switch_to.window(window_gl)
    data = file.getInfoProfile(index)
    try:
        field_data = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div[5]/div[2]/div[2]/div/form/fieldset[2]/div[2]/div/div/div[2]/label/div[2]/input')))
        field_data.send_keys(data[0])
        time.sleep(1)
        script = 'document.getElementsByClassName("fas fa-sync fa-spin ng-hide")[0].click()'
        driver.execute_script(script)
    except: pass

def loginGleamWithDiscord(driver):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.discord-background.popup-window')))
    window_gl = driver.current_window_handle
    numTab = driver.window_handles
    driver.execute_script("document.getElementsByClassName('discord-background popup-window')[0].click()")
    wait.until(EC.new_window_is_opened(numTab))

    try:
        window_dc = driver.window_handles[-1]
        driver.switch_to.window(window_dc)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'contents-3ca1mk')))
        driver.execute_script("document.getElementsByClassName('button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F')[0].click()")
    except: 
        pass
    finally:
        driver.switch_to.window(window_gl)



def doTask(driver, url, index):
    init(driver, url)
    wait = WebDriverWait(driver, 5)

    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'entry-method ')))
        #loginGleamWithTwitter(driver, index)
        #loginGleamWithDiscord(driver)
        #time.sleep(1.5)
   
#        try:
#            script = 'document.getElementsByClassName("text user-links entry-method-title ng-scope")[0].click()'
 #           driver.execute_script(script)
   #         
  #          numTab = driver.window_handles
  #          curr_tab = driver.current_window_handle
  #          script = 'document.getElementsByClassName("app-store-button ng-binding")[0].click()'
  #          driver.execute_script(script)
 #           WebDriverWait(driver, 5).until(EC.new_window_is_opened(numTab))
 #           driver.switch_to.window(driver.window_handles[-1])
  #          time.sleep(1)
 #           driver.close()
 #           driver.switch_to.window(curr_tab)
 #           time.sleep(1)
  #          script = 'document.getElementsByClassName("btn btn-primary")[1].click()'
 #           driver.execute_script(script)
  #          time.sleep(0.5)
  #      except: pass

        #task 1-2 tw
        for i in range(0, 2):
            try:
                script = 'document.getElementsByClassName("text user-links entry-method-title ng-scope")[%s].click()' %i
                driver.execute_script(script)
            except: pass

        #task 3-4 tweet, dis
        for i in range(2, 4):
            try:
                script = 'document.getElementsByClassName("text user-links entry-method-title ng-scope")[%s].click()' %i
                driver.execute_script(script)
                time.sleep(0.3)
                script = 'document.getElementsByClassName("btn btn-primary")[%s].click()' %i
                driver.execute_script(script)
            except: pass

        #check entries
        status = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="status ng-binding"]')))
        for i in range(0, 3):
            if int(status.text) >= 4: break
            time.sleep(3)
            status = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="status ng-binding"]')))

        #fill address (chua xong)
        try:
            Info = file.getInfoProfile(index)
            script = 'document.getElementsByClassName("text user-links entry-method-title ng-scope")[5].click()'
            driver.execute_script(script)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="em6633514Details"]'))).send_keys(Info[7])
            time.sleep(1.2)
            script = 'document.getElementsByClassName("btn btn-primary")[13].click()'
            driver.execute_script(script)
        except: pass

        try:
            for i in range(0,3):
                link_ref = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="share-link__link ng-binding"]')))
                link_ref = link_ref.text
                if link_ref != '': break
                time.sleep(3)
        except: link_ref = ''
        if link_ref != '':
            return link_ref
        return url
        
    except: raise Exception