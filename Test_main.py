import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://misleplav.ru'

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_cookie(browser):
    with webdriver.Chrome() as browser:
        browser.get(url)
        try:

            button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.ID, 'accept-cookies'))  # Ищем элемент
            )
            button.click()  # Нажимаем на элемент
            print("Тест успешен: Кнопка cookies нажата.")
        except Exception as e:
            print(f"Ошибка: {e}")

def test_enter(browser):
    with webdriver.Chrome() as browser:
        browser.get(url)
        try:
            button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-outline-light.mb-2.me-2.ms-3'))  # Ищем элемент
            )
            button.click()
            print("Тест успешен: Кнопка Enter нажата.")
        except Exception as e:
            print(f"Ошибка: {e}")

        input_username = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'id_username'))
        )
        input_username.send_keys('qwerty')

        input_password = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'id_password'))
        )
        input_password.send_keys('qpwoeiru')
        time.sleep(1)

        btn_sumbit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary.mt-3')
        btn_sumbit.click()


if __name__ == "__main__":
    with webdriver.Chrome() as browser:
        test_cookie(browser)
        test_enter(browser)





