import time
import unittest
import pytest
from selenium.webdriver import Chrome
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from Component.AdminPage import AdminPage
from Component.LoginPage import LoginPage


class Add_new_role(unittest.TestCase):
    
    def TC_001(self):
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
        Admin_page.click_add()
        time.sleep(5)
        Admin_page.select_add_user_user_role()
        Admin_page.enter_add_user_user_role()
        Admin_page.select_add_user_status()
        Admin_page.enter_add_user_status()
        Admin_page.employee_input('Test')
        time.sleep(5)
        Admin_page.select_employee()
        Admin_page.enter_employee()
        time.sleep(5)
        Admin_page.username_input('TestingAuto')
        Admin_page.add_user_password_input('Organization@123')
        Admin_page.add_user_confirm_password_input('Organization@123')
        time.sleep(5)
        Admin_page.click_save()
        time.sleep(5)

   

        driver.quit()

if __name__ == "__main__":
    unittest.main()