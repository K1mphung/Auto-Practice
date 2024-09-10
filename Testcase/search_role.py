import time
import unittest
import pytest
from selenium.webdriver import Chrome
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Component.LoginPage import LoginPage
from Component.AdminPage import AdminPage


class search_role(unittest.TestCase):
    @pytest.mark.regression
    def TC_003(self):
        driver = Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.email_input('Admin')
        login_page.password_input('admin123')
        login_page.click_login()
        time.sleep(5)

        Admin_page = AdminPage(driver)
        Admin_page.click_admin_page()
        time.sleep(5)
        Admin_page.click_org()
        Admin_page.click_general_info()
        time.sleep(5)

        valueHRM = Admin_page.get_attribute_value("value")
        print(valueHRM)
        self.assertFalse(valueHRM, "OrangeHRM")


        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()