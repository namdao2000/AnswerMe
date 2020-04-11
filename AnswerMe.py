from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pickle
from Question_id import question_id
import os
import socket


def initialise_browser():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.delete_all_cookies()
    driver.get("https://www.chegg.com/login/")
    sleep(2)
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("Loaded all cookies!")
    except Exception:
        print("No cookies detected, exiting.")
        exit()
    return driver


def screenshot(driver, url):
    if not os.path.exists("./screenshots"):
        os.mkdir("./screenshots")
    driver.get(url)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot("./screenshots/" + question_id(url) + ".png")
    print("Screenshot has been taken successfully.")


if __name__ == "__main__":
    firefox = initialise_browser()
    print("Browser initialised...")
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind(("127.0.0.1", 5000))
    while True:
        try:
            print("Stand by...")
            url = socket.recv(500).decode("utf-8").strip()
            print("received url :" + url)
            if url == "KILL":
                firefox.close()
                exit()

            screenshot(firefox, url)
            # Check to see if question ID already exists in the data base
            # pass it in the screenshot function
        except Exception as e:
            print(e)
            print("Error Handled. Continue on.")
            continue
