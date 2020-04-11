from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pickle
from Question_id import question_id
import os

def screenshot(driver, url):
    if not os.path.exists("./screenshots"):
        os.mkdir("./screenshots")
    driver.get(url)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot("./screenshots/" + question_id(url) + ".png")
    print("Screenshot has been taken successfully.")

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.delete_all_cookies()
driver.get("https://www.chegg.com/login/")
sleep(2)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
message = "https://www.chegg.com/homework-help/questions-and-answers/need-help-abstract-algebra-practice-test-circled-ones-need-help--numbers-1-6-7-8-11-14-tha-q28033053"

screenshot(driver, message)
