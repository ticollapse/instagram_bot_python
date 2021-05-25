
from pages import *
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

TIME_1 = 1
TIME_2 = 3
TIME_3 = 10


def init_browser():
    browser = webdriver.Firefox(executable_path=GeckoDriverManager(path='.').install())
    browser.implicitly_wait(5)
    return browser


def close_browser(browser):
    browser.close()

def main():
    browser = init_browser()

    homePage = HomePage(browser)

    loginPage = homePage.go_to_home_page()
    loginPage.login(username='xxx',password='xxx')
    loginPage.ignore_notification()

    searchPage = SearchPage(browser)
    searchPage.searchForTag("#sorteio")


    sleep(5)
    #close_browser(browser)

if __name__ == "__main__":
    main()