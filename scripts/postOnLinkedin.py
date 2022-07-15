import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class LinkedinBot:
    def __init__(self, username, password):

        self.driver = webdriver.Chrome('./chromedriver.exe')

        # self.base_url = 'https://www.linkedin.com'
        # self.login_url = self.base_url + '/login'
        # self.feed_url = self.base_url + '/feed'

        # self.username = username
        # self.password = password

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def login(self,username,password):
        self._nav('https://www.linkedin.com/login')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

    def post(self, text):
        """ Make a text post """
        self.driver.find_element_by_class_name('share-box-feed-entry__trigger').click()
        time.sleep(3)
        textbox = self.driver.find_elements_by_xpath('//p')[0].get_attribute("innerHTML")
        #print(textbox)
        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(5)

        self.driver.find_element_by_class_name('share-actions__primary-action').click()

def loginAndPostLinkedin(username,password,post_text):
    bot = LinkedinBot(username, password)
    try:
        bot.login(username, password)
        bot.post(post_text)
        LinkedInUsers = open("LinkedInUsers.txt", "a")
        LinkedInUsers.write("user="+username+" password="+password+"\n")
        LinkedInUsers.close()
    except NoSuchElementException:
        pass