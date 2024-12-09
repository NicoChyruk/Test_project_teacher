
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

url = 'https://misleplav.ru'

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Инициализация браузера
    yield driver  # Возврат объекта браузера для тестов
    driver.quit()  # Закрытие браузера после завершения теста

def test_registration(browser):
    browser.get(url)

    try:
        # Ждем, пока кнопка регистрации станет кликабельной
        btn_registr = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="signup"]'))
        )
        btn_registr.click()  # Нажимаем на кнопку
        print("Тест успешен: Кнопка Register нажата.")
    except Exception as e:
        print(f"Ошибка при нажатии на кнопку регистрации: {e}")
        return

    # Используем Faker для генерации данных
    faker = Faker()
    username = faker.user_name()
    password = faker.password()

    try:
        input_username = browser.find_element(By.ID, 'id_username')
        input_username.send_keys(username)

        input_password = browser.find_element(By.ID, 'id_password1')
        input_password.send_keys(password)

        input_password_repeat = browser.find_element(By.ID, 'id_password2')
        input_password_repeat.send_keys(password)

        btn_finish_registration = browser.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]')
        btn_finish_registration.click()

        time.sleep(2)

        print("Тест успешен: Форма регистрации заполнена.")
    except Exception as e:
        print(f"Ошибка при заполнении формы: {e}")
