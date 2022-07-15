import time
from tkinter.tix import Tree
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class FacebookBot:
    def __init__(self, username, password):

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.base_url = 'https://www.facebook.com'
        self.login_url = self.base_url
        self.feed_url = self.base_url +"/profile"

        self.username = username
        self.password = password

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def login(self,username,password):
        self._nav(self.login_url)
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'התחבר/י')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//a[contains(@aria-label,"דף הבית")]').click() #check if the login worked
        
    
def loginFacebook(username,password):
    bot = FacebookBot(username, password)
    try:
        bot.login(username, password)
        FacebookUsers = open("FacebookUsers.txt", "a")
        FacebookUsers.write("user="+username+" password="+password+"\n")
        FacebookUsers.close()
    except NoSuchElementException:
        pass

