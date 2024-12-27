import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

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
            EC.element_to_be_clickable((By.CLASS_NAME, "fas.fa-user-plus.me-1"))
        )
        btn_registr.click()
        print("Тест успешен: Кнопка Register нажата.")
    except Exception as e:
        raise Exception(f"Ошибка при нажатии на кнопку регистрации: {e}")

def test_registration_correct(browser):
    navigate_to_registration_page(browser)

    faker = Faker()
    email = faker.email()
    password = faker.password()

    input_email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_email"))
    )
    input_email.send_keys(email)

    input_password = browser.find_element(By.ID, "id_password1")
    input_password.send_keys(password)

    input_password_repeat = browser.find_element(By.ID, "id_password2")
    input_password_repeat.send_keys(password)

    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Зарегистрироваться"]'))
    )

    actions = ActionChains(browser)
    actions.move_to_element(button).perform()
    button.click()

    text_element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h2"))
    )
    assert "Приветствуем тебя!" in text_element.text

def test_registration_teacher(browser):
    navigate_to_registration_page(browser)

    faker = Faker()
    email = faker.email()
    password = faker.password()

    input_email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_email"))
    )
    input_email.send_keys(email)

    input_password = browser.find_element(By.ID, "id_password1")
    input_password.send_keys(password)

    input_password_repeat = browser.find_element(By.ID, "id_password2")
    input_password_repeat.send_keys(password)

    input_checkbox = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_is_tutor"))
    )

    actions = ActionChains(browser)
    actions.move_to_element(input_checkbox).perform()
    input_checkbox.click()

    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Зарегистрироваться"]'))
    )

    actions = ActionChains(browser)
    actions.move_to_element(button).perform()
    button.click()

    text_element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h2"))
    )
    assert "Приветствуем тебя, репетитор!" in text_element.text