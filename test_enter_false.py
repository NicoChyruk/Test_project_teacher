from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://misleplav.ru'


def test_click_enter(browser):
    browser.get(url)
    try:
        enter_element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "nav-link"))
        )
        enter_element.click()
    except Exception as e:
        raise Exception(f"'Ошибка при клике на кнопку Войти:' {e}")

def test_password_empty(browser):
    test_click_enter(browser)

    email_text = browser.find_element(By.ID, "id_username")
    email_text.send_keys('nikolay228@gmail.com')

    password_text = browser.find_element(By.ID, "id_password")
    password_text.send_keys('')

    login = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

    error_text_empty_password = browser.find_element(By.ID, 'error_1_id_password')

    assert "Обязательное поле." in error_text_empty_password.text

def test_password_not_correct(browser):
    test_click_enter(browser)

    email_text = browser.find_element(By.ID, "id_username")
    email_text.send_keys('nikolay228@gmail.com')

    password_text = browser.find_element(By.ID, "id_password")
    password_text.send_keys('sdasdads')

    login = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

    error_text_not_correct_password = browser.find_element(By.CLASS_NAME, 'alert.alert-block.alert-danger')

    assert ("Пожалуйста, введите правильные email и пароль. Оба поля могут быть чувствительны к регистру." in
            error_text_not_correct_password.text)


def test_email_password_empty(browser):
    test_click_enter(browser)

    email_text = browser.find_element(By.ID, "id_username")
    email_text.send_keys('')

    password_text = browser.find_element(By.ID, "id_password")
    password_text.send_keys('')

    login = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

    error_text_empty_password = browser.find_element(By.ID, 'error_1_id_username')
    assert "Обязательное поле." in error_text_empty_password.text

    error_text_empty_password = browser.find_element(By.ID, 'error_1_id_password')
    assert "Обязательное поле." in error_text_empty_password.text

def test_empty_password(browser):
    test_click_enter(browser)

    email_text = browser.find_element(By.ID, "id_username")
    email_text.send_keys('')

    password_text = browser.find_element(By.ID, "id_password")
    password_text.send_keys('AdnanYui1')

    login = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

    error_text_empty_password = browser.find_element(By.ID, 'error_1_id_username')
    assert "Обязательное поле." in error_text_empty_password.text

