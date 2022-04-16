from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestTry(unittest.TestCase):

    def test0ne(self):
        self.browser = webdriver.Chrome()
        link1 = 'http://suninjuly.github.io/registration1.html'
        self.browser.get(link1)
        self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('xuy')
        self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('xuy')
        self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('xuy')
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(text, 'Congratulations! You have successfully registered!', 'You lose!')
        self.browser.close()

    def testTwo(self):
        self.browser = webdriver.Chrome()
        link2 = 'http://suninjuly.github.io/registration2.html'
        self.browser.get(link2)
        self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]').send_keys('xuy')
        self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('xuy')
        self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('xuy')
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(text, 'Congratulations! You have successfully registered!', 'You lose!')
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
