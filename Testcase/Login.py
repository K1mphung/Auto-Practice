import time
import unittest
from selenium.webdriver import Chrome
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Component.LoginPage import LoginPage


class Add_new_role(unittest.TestCase):
    def test_login_002(self):
        driver = Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.email_input('Admin')
        login_page.password_input('admin123')
        login_page.click_login()
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()