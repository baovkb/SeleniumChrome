import time
from selenium import webdriver
import undetected_chromedriver as webdriver

class Tabs():
    def __init__(self) -> None:
        self.tab_id = None

    def openTab(self, driver:webdriver, url: str):
        try:
            #driver.tab_new(url)
            try:
                driver.switch_to.window(driver.window_handles[-1])
                driver.execute_script("window.open()")
            except:
                driver.tab_new(url)
            driver.switch_to.window(driver.window_handles[-1])

            driver.get(url)
            time.sleep(0.5)
            self.tab_id = driver.current_window_handle
        except: pass

    def openTabs(self, driver:webdriver, urls: list):
        for url in urls:
            self.openTab(driver, url)

    def closeTab(self, driver:webdriver):
        if self.selectTab(driver) is True:
            driver.close()
        self.tab_id = None
        driver.switch_to.window(driver.window_handles[0])

    def selectTab(self, driver:webdriver) -> bool:
        if self.tab_id is None: return False
        i = 0
        for j in driver.window_handles:
            if j == self.tab_id:
                driver.switch_to.window(driver.window_handles[i])
                return True
            i = i + 1
        return False