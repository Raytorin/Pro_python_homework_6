from selenium import webdriver
import time
import requests
import os


abspath_to_driver = os.path.abspath("firefoxdriver/geckodriver")


def auth_page(login, password, abspath):
    browser = webdriver.Firefox(executable_path=abspath)
    try:
        browser.get('https://passport.yandex.ru/auth/add')
        time.sleep(3)
        login_input = browser.find_element("id", "passp-field-login")
        login_input.clear()
        login_input.send_keys(login)
        time.sleep(3)

        login_button = browser.find_element("id", "passp:sign-in").click()
        time.sleep(3)

        password_input = browser.find_element("id", "passp-field-passwd")
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(3)

        password_botton = browser.find_element("id", "passp:sign-in").click()
        time.sleep(3)

        response = requests.get(browser.current_url)
        time.sleep(3)
        return str(response.status_code)
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':
    login_user = ''
    password_user = ''
    print(auth_page(login_user, password_user, abspath_to_driver))
