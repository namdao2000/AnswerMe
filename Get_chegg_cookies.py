from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pickle
from random import uniform
from Credentials import *
import os

def send_slower(element, text):
    for character in text:
        element.send_keys(character)
        sleep(uniform(0.3, 0.4))


def get_session_cookie(usr, passwd):
    if not os.path.exists("cookies.pkl"):
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(options=options)
        browser.delete_all_cookies()
        browser.get("https://www.chegg.com/login/")
        sleep(1)
        send_slower(browser.find_element_by_id("emailForSignIn"), usr)
        send_slower(browser.find_element_by_id("passwordForSignIn"), passwd)
        browser.find_element_by_name("login").click()
        sleep(5)
        pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

if __name__ == "__main__":
    get_session_cookie(username, passwd)

