from re import U
import time
import urllib.request
import webbrowser
from selenium import webdriver


# set web driver for chrome
driver = webdriver.Chrome()

# enter url of website (github)
url = "https://github.com/"

# call driver to get webpage
driver.get(url)



#webbrowser.open("https://github.com/")
#get_url = urllib.request.urlopen('https://github.com/')
