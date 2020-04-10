from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pickle

options = Options()
options.headless = False
browser = webdriver.Firefox(options=options)
browser.delete_all_cookies()

browser.get("https://www.chegg.com/login/")

# Make sure we navigate to the original website where the cookie is retrieved first. Then , we load in the cookie and
# Access other sites.

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
sleep(1)

browser.get("https://www.chegg.com/homework-help/questions-and-answers/question-1-05-pts-suppose-following-two-lists-fruits-apple-banana-orange-banana-cherry-lem-q35338475")
print("All done")

# def searchChegg(link):
