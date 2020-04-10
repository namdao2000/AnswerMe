from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pickle

def screenshot(browser, url, file):
    browser.get(url)
    S = lambda X: browser.execute_script('return document.body.parentNode.scroll'+X)
    browser.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    browser.find_element_by_tag_name('body').screenshot(file)

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.delete_all_cookies()
# Make sure we navigate to the original website where the cookie is retrieved first. Then , we load in the cookie and
# Access other sites.
browser.get("https://www.chegg.com/login/")

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
sleep(1)

screenshot(browser, "https://www.chegg.com/homework-help/questions-and-answers/question-1-1-pts-true-false-apple-added-twice-set-added-set-b-set-set-b-would-considered-d-q35338479", "./screenshots/question11.png")
print("All done")

