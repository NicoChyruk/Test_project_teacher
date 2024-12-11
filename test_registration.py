import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import logging

logging.basicConfig(level=logging.INFO)

url = 'https://misleplav.ru'

LOCATORS = {
    "signup_button": (By.CSS_SELECTOR, '[data-testid="signup"]'),
    "username_input": (By.ID, 'id_username'),
    "password_input": (By.ID, 'id_password1'),
    "password_repeat_input": (By.ID, 'id_password2'),
    "submit_button": (By.CSS_SELECTOR, '[data-testid="submit-button"]'),
    "success_alert": (By.CSS_SELECTOR, ".alert.alert-success"),
    "tutor_checkbox": (By.ID, 'id_is_tutor'),
}

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def fill_registration_form(browser, username, password, is_teacher=False):
    browser.find_element(*LOCATORS["username_input"]).send_keys(username)
    browser.find_element(*LOCATORS["password_input"]).send_keys(password)
    browser.find_element(*LOCATORS["password_repeat_input"]).send_keys(password)
    if is_teacher:
        browser.find_element(*LOCATORS["tutor_checkbox"]).click()
    browser.find_element(*LOCATORS["submit_button"]).click()

def check_success_message(browser, expected_message):
    alert = browser.find_element(*LOCATORS["success_alert"])
    assert expected_message in alert.text, \
        f"Сообщение отличается: ожидалось '{expected_message}', получено '{alert.text}'"
    logging.info("Сообщение о регистрации подтверждено.")

@pytest.mark.registration
def test_registration(browser):
    browser.get(url)
    faker = Faker()
    username = faker.user_name()
    password = faker.password()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(LOCATORS["signup_button"])).click()
    fill_registration_form(browser, username, password)
    check_success_message(browser, 'Вы успешно зарегистрировались!')

@pytest.mark.registration
def test_registration_teacher(browser):
    browser.get(url)
    faker = Faker()
    username = faker.user_name()
    password = faker.password()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(LOCATORS["signup_button"])).click()
    fill_registration_form(browser, username, password, is_teacher=True)
    check_success_message(browser, 'Вы успешно зарегистрировались, а так же получаете бесплатный премиум на 3 дня!')

