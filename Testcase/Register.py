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
        time.sleep(5)


        login_page = LoginPage(driver)
        login_page.frame_switch()
        login_page.robot()

        login_page.enter_Login_page()

        Register_page = LoginPage(driver)
        Register_page.enter_Register_page()

        Register_page.enter_Gender()
        Register_page.enter_fist_name('Phung')
        Register_page.enter_last_name('Nguyen')
        time.sleep(5)

        Register_page.day_select('6')
        Register_page.month_select('6')
        Register_page.year_select('1997')

        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()