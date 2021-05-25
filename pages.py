from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_home_page(self):
        self.browser.get('https://www.instagram.com/')
        sleep(2)
        return LoginPage(self.browser)

class LoginPage:
    def __init__(self,browser):
        self.browser = browser
        self.time_to_loggin = 3

    def login(self, username, password):
        username_input = self.browser.find_element_by_xpath("//input[@name='username']")
        password_input = self.browser.find_element_by_xpath("//input[@name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_xpath("//form[@id='loginForm']//button[@type='submit']")
        login_button.click()
        sleep(self.time_to_loggin)

    def ignore_notification(self):
        delay_to_button_show_up = 1
        sleep(delay_to_button_show_up)
        try:
            ignore_button = self.browser.find_elements_by_class_name("mt3GC")
            print(ignore_button)
            ignore_button.click()
            print("Notificação ignorada!")
        except NoSuchElementException as e:
            print("Nenhuma mensagem de notificação foi ignorada!")

class SearchPage():
    def __init__(self,browser):
        self.browser = browser

    def searchForTag(self,tag):
        search_input = self.browser.find_element_by_xpath("//html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search_input.send_keys(tag)
        self.browser.find_element_by_xpath("//html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]").click()
        #search_input.send_keys(Keys.RETURN)
        #search_input.send_keys(Keys.ENTER)

