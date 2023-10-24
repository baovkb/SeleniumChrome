from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import IOFile as file
import random, time, pf

class Twitter():
    def __init__(self, gologin:pf.ProfileGL):
        gologin.openTab('https://mobile.twitter.com')

    def isLogin(self, gologin:pf.ProfileGL) -> bool:
        try:
            WebDriverWait(gologin.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Account menu']")))
            return True
        except: return False

    def formatLink(self, link: list) -> list:
        for i in range(0, len(link)):
            if link[i].find('mobile') == -1:
                link[i] = link[i][0:8] + 'mobile.' + link[i][8:]
        return link
    
    def closeTab(self, gologin:pf.ProfileGL):
        gologin.selectTab(self.tab_id)
        gologin.closeTab()
        self.tab_id = None

    def follow(self, gologin:pf.ProfileGL, link:list):
        driver = gologin.driver
        for i in link:
            gologin.navigate(i)     
            try:
                follw_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text() = 'Follow' or text() = 'Following']")))
                if follw_button.text == 'Follow':
                    driver.execute_script("arguments[0].click();", follw_button)
                break
            except: pass
            time.sleep(0.5)

    def login(self, gologin: pf.ProfileGL, password):
        driver = gologin.driver
        wait = WebDriverWait(driver, 5)
        username = file.getInfoProfile(gologin.profile_id)
        username = username['userTwitter']
        gologin.navigate('https://mobile.twitter.com/i/flow/login')
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username"]'))).send_keys(username)
            element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')))
            for j in range(len(element)):
                if element[j].get_attribute('innerHTML') == 'Next': 
                    driver.execute_script("arguments[0].click();", element[j]) 
                    break
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]'))).send_keys(password)
            time.sleep(1)
            element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')))
            for j in range(len(element)):
                if element[j].get_attribute('innerHTML') == 'Log in': 
                    driver.execute_script("arguments[0].click();", element[j]) 
                    break
        except: pass


    def like(self, gologin:pf.ProfileGL, link:list):
        driver = gologin.driver
        for i in link:
            gologin.navigate(i)
            try:
                like_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like' or @aria-label='Liked']")))
                if like_button.accessible_name == 'Like':
                    driver.execute_script("arguments[0].click();", like_button)
            except: pass
            time.sleep(0.5)

    def retweet(self, gologin:pf.ProfileGL, link:list):
        driver = gologin.driver
        for i in link:
            gologin.navigate(i)
            try:
                retweet_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet' or @aria-label='Retweeted']")))
                if retweet_button.accessible_name == 'Retweet':
                    driver.execute_script("arguments[0].click();", retweet_button)

                    #retweet confirm
                    retweet_confirm = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweetConfirm']")))
                    driver.execute_script("arguments[0].click();", retweet_confirm)
                break
            except: pass
            time.sleep(0.5)


    def quoteTweet(self, gologin:pf.ProfileGL, link:list, numTag = 0) -> list:
        driver = gologin.driver
        llink_quote = []
        for i in link:
            text = random_text(numTag)
            gologin.navigate(i)
            try:
                retweet_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet' or @aria-label='Retweeted']")))
                driver.execute_script("arguments[0].click();", retweet_button)

                try:
                    #quote retweet press
                    quote_confirm = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Quote Tweet']")))
                    driver.execute_script("arguments[0].click();", quote_confirm)

                    #dismis popup
                    try:
                        WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.XPATH, '//span[text() = "Maybe later"]/../..'))).click()
                    except: pass

                    #quote retweet confirm
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']"))).send_keys(text)
                    tweet_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButton']")))
                    driver.execute_script("arguments[0].click();", tweet_button)
                    time.sleep(1)
                    for j in range(0, 3):
                        if (driver.current_url).find('compose/tweet') == -1:
                            break
                        time.sleep(2)

                    llink_quote.append(self.getNewestTweet(gologin))
                except: pass
            except: pass
        return llink_quote

    def tweetByLink(self, gologin:pf.ProfileGL, link:list):
        driver = gologin.driver
        for i in link:
            gologin.navigate(i)
            try:
                tweet_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetButton']")))
                driver.execute_script("arguments[0].click();", tweet_button)
                time.sleep(1)
                for j in range(0, 3):
                    if (driver.current_url).find('/intent/') == -1:
                        break
                    time.sleep(2)
            except: pass
            time.sleep(0.5)


    def getNewestTweet(self, gologin: pf.ProfileGL) -> str:
        Info = file.getInfoProfile(gologin.profile_id)
        driver = gologin.driver
        driver.get(Info['linkTwitter'])
        #get link quote retweet
        tweet_quote = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetText']")))
        driver.execute_script("arguments[0].click();", tweet_quote)
        time.sleep(1)
        return self.formatLink([driver.current_url])[0]
    

    def commment(self, gologin: pf.ProfileGL, numTag = 0):
        driver = gologin.driver
        Info = file.getInfoProfile(gologin.profile_id)
        # text = random_text(numTag)
        # text = text + '\n' + Info['evm']
        text = Info['evm']

        for i in range(0, 3):
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']"))).send_keys(text)

                #add picture
                # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Add photos or video"]'))).click()
                # time.sleep(0.5)
                # import autoit
                # autoit.win_activate('Open')
                # autoit.control_send("Open","Edit1",r"D:\Downloads\airdrop.jpeg")
                # time.sleep(0.5)
                # autoit.control_send("Open","Edit1","{ENTER}")

                #confirm tweet
                tweet_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetButtonInline']")))
                driver.execute_script("arguments[0].click();", tweet_button)
                time.sleep(2)
                break
            except: pass
    

def random_text(numTag = 0):
    try:
        tag = ''
        if numTag > 0:
            count = file.countProfileInfo()
            for i in range(0, numTag):
                tmp1 = random.randint(1, count)
                tmp2 = file.getInfoProfile(tmp1)
                tag = tag  + tmp2['userTwitter'] + ' '

        count = file.countTweetText()
        tmp1 = random.randint(1, count)
        txt = file.getTweetText(tmp1)
        txt = txt + ' ' + tag
        return txt
    except: raise Exception

