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

def test_enter_correct(browser):
    test_click_enter(browser)

    email_text = browser.find_element(By.ID, "id_username")
    email_text.send_keys('nikolay228@gmail.com')

    password_text = browser.find_element(By.ID, "id_password")
    password_text.send_keys('AdnanYui1')

    login = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

    expected_url = "https://misleplav.ru/listings/list/"
    current_url = browser.current_url

    if current_url == expected_url:
        print("Открыта нужная страница!")
    else:
        print("Это не та страница!")

def test_enter_correct_teacher(browser):
    test_click_enter(browser)

    email_text = browser.find_element(By.ID, "id_username")
    email_text.send_keys('teacher228@gmail.com')

    password_text = browser.find_element(By.ID, "id_password")
    password_text.send_keys('AdnanYui1')

    login = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

    expected_url = "https://misleplav.ru/listings/list/"
    current_url = browser.current_url

    if current_url == expected_url:
        print("Открыта нужная страница!")
    else:
        print("Это не та страница!")


