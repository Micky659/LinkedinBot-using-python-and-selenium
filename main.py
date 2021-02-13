from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_id('username')
        password_input = self.browser.find_element_by_id('password')
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[contains(text(), 'Sign in')]")
        login_button.click()
        sleep(3)
        #if skip == self.browser.find_element_by_xpath("//a[contains(text(), 'Skip')]"):
        #   skip.click()
        sleep(5)    

class Bot:
    def __init__(self, browser):
        self.browser = browser

    def people(self, texts, li, num):
        #self.browser.find_element_by_xpath("/html/body/div[8]/aside/div[1]/header/section[2]/button[2]/li-icon/svg").click()
        #sleep(2)
        search = self.browser.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(texts)
        sleep(3)
        search.send_keys(Keys.DOWN)
        sleep(1)
        search.send_keys(Keys.DOWN)
        sleep(1)
        search.send_keys(Keys.ENTER)
        sleep(3)
        # self.browser.find_element_by_id("ember1187").click()
        # self.browser.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[1]/nav/div/div[1]/div/div[2]/ul/li[2]").click()
        # sleep(3)
        self.filter(li, num)

    def filter(self, li, num):
        location = browser.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[1]/nav/div/div[1]/div/div[2]/ul/li[4]/div")
        location.click()
        for n in li:
            find = self.browser.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[1]/nav/div/div[1]/div/div[2]/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/div/div/div/input")
            find.send_keys(n)
            sleep(1)
            find.send_keys(Keys.DOWN)
            sleep(1)
            find.send_keys(Keys.ENTER)
            sleep(2)
        element = self.browser.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[1]/nav/div/div[1]/div/div[2]/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span")
        element.click()      
        sleep(3)
        self.connect(num)

    def connect(self, num):
        conn = self.browser.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
        for i in conn[0:num]:
            i.click()
            self.browser.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
            sleep(1)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.linkedin.com/')

    def enter_page(self):
        self.browser.find_element_by_xpath("//a[contains(text(), 'Sign in')]").click()
        sleep(2)
        return LoginPage(self.browser)


def Test(browser, texts, li, num):
    home_page = HomePage(browser)
    login_page = home_page.enter_page()

    #Enter login credential below in place of username and password
    login_page.login("Username", "Password")

    bot = Bot(browser)
    bot.people(texts, li, num)

li = list()
texts = input("Enter searching criterion ")
if ( len(texts) < 1 ) : texts = 'Machine learning'
user = input("Enter locations ")
num = int(input("Enter number of people to connect to "))
li = user.split()
browser = webdriver.Firefox()
browser.implicitly_wait(5)
Test(browser, texts, li, num)

sleep(10)

browser.close()