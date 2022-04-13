from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class test3_2(unittest.TestCase):
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/registration1.html'
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('xuy')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('xuy')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('xuy')
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()