from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
browser = webdriver.Firefox(options=options)
browser.get("https://www.chegg.com/homework-help/questions-and-answers/discussed-class-following-implementation-doublylinkedlist-conductor-hasnext-doesn-t-work-c-q26693373?trackid=437bf39de055&strackid=0400b1737125")
print("All done")

# def searchChegg(link):
