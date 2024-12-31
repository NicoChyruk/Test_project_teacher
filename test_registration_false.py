
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

url = 'https://misleplav.ru'

def navigate_to_registration_page(browser):
    browser.get(url)
    try:
        btn_registr = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fas.fa-user-plus.me-1"))
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

def fill_registration_form(browser, email, password, password_repeat):

    input_email = browser.find_element(By.ID, 'id_email')
    input_email.send_keys(email)
    time.sleep(0.2)

    input_password = browser.find_element(By.ID, 'id_password1')
    input_password.send_keys(password)
    time.sleep(0.1)

    input_password_repeat = browser.find_element(By.ID, 'id_password2')
    input_password_repeat.send_keys(password_repeat)
    time.sleep(0.1)

    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Зарегистрироваться"]'))
    )

    actions = ActionChains(browser)
    actions.move_to_element(button).perform()
    button.click()


def test_email_false(browser):
    navigate_to_registration_page(browser)

    try:
        fill_registration_form(browser, 'asd', 'Adin12dva', 'Adin12dva')
        check_error_message(browser, 'error_1_id_email',
                            "Введите правильный адрес электронной почты.",
                            "Тест успешен: Ошибка 'Введённый пароль слишком широко распространён.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise

def test_email_empty(browser):
    navigate_to_registration_page(browser)

    try:
        fill_registration_form(browser, '', 'Adin12dva', 'Adin12dva')
        check_error_message(browser, 'error_1_id_email',
                            "Обязательное поле.",
                            "Тест успешен: Ошибка 'Введённый пароль слишком широко распространён.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise


def test_registration_false(browser):
    navigate_to_registration_page(browser)

    try:
        faker = Faker()
        email = faker.email()
        fill_registration_form(browser, email, 'password', 'password')
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
        email = faker.email()
        fill_registration_form(browser, email, 'password', 'password12345')
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
        email = faker.email()
        fill_registration_form(browser, email, '123456789055', '123456789055')
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
        email = faker.email()
        fill_registration_form(browser, email, 'ChayWn', 'ChayWn')
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
        email = faker.email()
        fill_registration_form(browser, email, 'ChayWn', '')
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
        email = faker.email()
        fill_registration_form(browser, email, '', 'ChayWn')
        check_error_message(browser, 'error_1_id_password1',
                            "Обязательное поле.",
                            "Тест успешен: Ошибка 'Обязательное поле.' отображается.")
    except Exception as e:
        print(f"Ошибка во время теста: {e}")
        raise


