import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



link1 = 'https://stepik.org/lesson/236895/step/1'
link2 = 'https://stepik.org/lesson/236896/step/1'
link3 = 'https://stepik.org/lesson/236897/step/1'
link4 = 'https://stepik.org/lesson/236898/step/1'
link5 = 'https://stepik.org/lesson/236899/step/1'
link6 = 'https://stepik.org/lesson/236903/step/1'
link7 = 'https://stepik.org/lesson/236904/step/1'
link8 = 'https://stepik.org/lesson/236905/step/1'


@pytest.fixture(scope="class")
def browser():
    print('\nStarting browser...')
    browser = webdriver.Chrome()
    yield browser
    print('\nQuiting browser...')
    browser.quit()


@pytest.mark.parametrize('link', [link1, link2, link3, link4, link5, link6, link7, link8])
class TestMainPage:
    def test_params(self, browser, link):
        browser.implicitly_wait(7)
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.find_element(By.TAG_NAME, 'textarea').send_keys(f'{answer}')
        browser.find_element(By.CSS_SELECTOR, 'button[class="submit-submission"]').click()
        result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        assert result == "Correct!", f'Текст из фидбека не совпадает. Должно быть: "Correct!", есть: {result}'

# print(answer)

#21.224319567908218
#21.224319596991027