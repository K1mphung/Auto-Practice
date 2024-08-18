import time
import unittest
from selenium.webdriver import Chrome
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Component.LoginPage import LoginPage


class Register(unittest.TestCase):
    def test_successful_login(self):
        driver = Chrome()
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.enter_username('qa-vn-picking-app-02@stor.ai')
        login_page.enter_password('t123456')
        login_page.enter_retailer_id('6')
        login_page.click_login()

        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()