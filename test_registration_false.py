import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

url = 'https://misleplav.ru'

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def navigate_to_registration_page(browser):
    browser.get(url)
    try:
        btn_registr = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="signup"]'))
        )
        btn_registr.click()
        print("Тест успешен: Кнопка Register нажата.")
    except Exception as e:
        raise Exception(f"Ошибка при нажатии на кнопку регистрации: {e}")


def check_error_message(browser, element_id, expected_message, success_message=None):

    error_element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, element_id))
    )
    error_message = error_element.text
    assert expected_message in error_message, f"Сообщение об ошибке не найдено или текст отличается: {error_message}"
    if success_message:
        print(success_message)

def fill_registration_form(browser, email, username, password, password_repeat):

    input_email = browser.find_element(By.ID, 'id_email')
    input_email.send_keys(email)
    time.sleep(1)

    input_username = browser.find_element(By.ID, 'id_first_name')
    input_username.send_keys(username)
    time.sleep(1)

    input_password = browser.find_element(By.ID, 'id_password1')
    input_password.send_keys(password)
    time.sleep(1)

    input_password_repeat = browser.find_element(By.ID, 'id_password2')
    input_password_repeat.send_keys(password_repeat)
    time.sleep(1)

    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Зарегистрироваться"]'))
    )

    # Скроллим к элементу с помощью ActionChains
    actions = ActionChains(browser)
    actions.move_to_element(button).perform()

    # Кликаем на элемент
    button.click()


def test_registration_false(browser):
    navigate_to_registration_page(browser)

    try:
        faker = Faker()
        username = faker.user_name()
        email = faker.email()
        fill_registration_form(browser, email, username, 'password', 'password')
        check_error_message(browser, 'error_1_id_password2',
                            "Введённый пароль слишком широко распространён.",
                            "Тест успешен: Ошибка 'Введённый пароль слишком широко распространён.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

def test_registration_false_repeat(browser):

    navigate_to_registration_page(browser)

    try:
        faker = Faker()
        username = faker.user_name()
        email = faker.email()
        fill_registration_form(browser, email, username, 'password', 'password12345')
        check_error_message(browser, 'error_1_id_password2',
                            "Введенные пароли не совпадают.",
                            "Тест успешен: Ошибка 'Введенные пароли не совпадают.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

def test_registration_false_int(browser):

    navigate_to_registration_page(browser)

    try:
        faker = Faker()
        username = faker.user_name()
        email = faker.email()
        fill_registration_form(browser, email, username, '123456789055', '123456789055')
        check_error_message(browser, 'error_1_id_password2',
                            "Введённый пароль состоит только из цифр.",
                            "Тест успешен: Ошибка 'Введённый пароль состоит только из цифр.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

def test_registration_false_sum_int(browser):

    navigate_to_registration_page(browser)

    try:
        faker = Faker()
        username = faker.user_name()
        email = faker.email()
        fill_registration_form(browser, email, username, 'ChayWn', 'ChayWn')
        check_error_message(browser, 'error_1_id_password2',
                            "Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.",
                            "Тест успешен: Ошибка 'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

def test_registration_without_first_password(browser):

    navigate_to_registration_page(browser)

    try:
        faker = Faker()
        username = faker.user_name()
        email = faker.email()
        fill_registration_form(browser, email, username, 'ChayWn', '')
        check_error_message(browser, 'error_1_id_password2',
                            "Обязательное поле.",
                            "Тест успешен: Ошибка 'Обязательное поле.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

def test_registration_without_repeat_password(browser):

    navigate_to_registration_page(browser)

    try:
        faker = Faker()
        username = faker.user_name()
        email = faker.email()
        fill_registration_form(browser, email, username, '', 'ChayWn')
        check_error_message(browser, 'error_1_id_password1',
                            "Обязательное поле.",
                            "Тест успешен: Ошибка 'Обязательное поле.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

def test_registration_username_errors(browser):

    navigate_to_registration_page(browser)

    try:
        fill_registration_form(browser, 'mikalai@gmail.com', 'Mikalai', 'ChayWnaa', 'ChayWnaa')
        check_error_message(browser, 'error_1_id_email',
                            "Пользователь с таким Email уже существует.",
                            "Тест успешен: Ошибка 'Пользователь с таким именем уже существует.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

