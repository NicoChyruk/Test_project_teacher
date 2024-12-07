from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://misleplav.ru'

with webdriver.Chrome() as browser:
    browser.get(url)