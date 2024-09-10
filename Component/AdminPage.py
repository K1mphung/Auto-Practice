from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import traceback
class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_page = (By.XPATH,'//span[contains(.,"Admin")]/parent::a')
        self.user_role_search_box = (By.XPATH,'(//div[contains(@class,"select-text-input")])[1]')
        self.user_role_search_box = (By.XPATH,'//label[contains(text(),"User Role")]/ancestor::div[contains(@class,"oxd-input-field")]//div[contains(@class,"select-text-input")]')
        self.search_button = (By.XPATH,'//div[contains(@class,"oxd-form-actions")]//button[contains(@type,"submit")]')
        self.get_text = (By.XPATH,'div[class="orangehrm-horizontal-padding orangehrm-vertical-padding"] span[class="oxd-text oxd-text--span"]')
        self.add_button = (By.XPATH,'//button[normalize-space()="Add"]')
        self.add_user_user_role = (By.XPATH,'//label[contains(text(),"User Role")]/ancestor::div[contains(@class,"input-field-bottom-space")]//div[contains(@class,"oxd-select-text-input")]')
        self.add_user_status = (By.XPATH,'//label[contains(text(),"Status")]/ancestor::div[contains(@class,"input-field-bottom-space")]//div[contains(@class,"oxd-select-text-input")]')
        self.add_user_employee_name = (By.XPATH,'//input[contains(@placeholder,"Type for hints")]')
        self.add_user_username = (By.XPATH,'//label[contains(text(),"Username")]/ancestor::div[contains(@class,"input-field-bottom-space")]//input[contains(@class,"oxd-input--active")]')
        self.add_user_password = (By.XPATH,'(//input[@type="password"])[1]')
        self.add_user_confirm_password = (By.XPATH,'(//input[@type="password"])[2]')
        self.save_button = (By.XPATH,'//button[contains(@type,"submit")]')
        self.organization = (By.XPATH,'//header//span[text()="Organization "]')
        self.general_info = (By.XPATH,'//header//a[text()="General Information"]')
        self.org_name = (By.XPATH,'//div[contains(@class,"oxd-input-group") and .//label[.="Organization Name"]]//input')




    def click_admin_page(self):
        self.driver.find_element(*self.admin_page).click()

    def select_user_role(self):
        self.driver.find_element(*self.user_role_search_box).send_keys(Keys.ARROW_DOWN)

    def enter_user_role(self):
        self.driver.find_element(*self.user_role_search_box).send_keys(Keys.ENTER)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()
    
    def get_attribute_text(self):
        return self.driver.find_element(*self.get_text).text()

    def click_add(self):
        self.driver.find_element(*self.add_button).click()

    def select_add_user_user_role(self):
        self.driver.find_element(*self.add_user_user_role).send_keys(Keys.ARROW_DOWN)

    def enter_add_user_user_role(self):
        self.driver.find_element(*self.add_user_user_role).send_keys(Keys.ENTER)
    
    def select_add_user_status(self):
        self.driver.find_element(*self.add_user_status).send_keys(Keys.ARROW_DOWN)

    def enter_add_user_status(self):
        self.driver.find_element(*self.add_user_status).send_keys(Keys.ENTER)

    def employee_input(self, employee):
        self.driver.find_element(*self.add_user_employee_name).send_keys(employee)

    def select_employee(self):
        self.driver.find_element(*self.add_user_employee_name).send_keys(Keys.ARROW_DOWN)

    def enter_employee(self):
        self.driver.find_element(*self.add_user_employee_name).send_keys(Keys.ENTER)

    def username_input(self, username):
        self.driver.find_element(*self.add_user_username).send_keys(username)

    def add_user_password_input(self, add_user_password):
        self.driver.find_element(*self.add_user_password).send_keys(add_user_password)

    def add_user_confirm_password_input(self, confirmpassword):
        self.driver.find_element(*self.add_user_confirm_password).send_keys(confirmpassword)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def click_org(self):
        self.driver.find_element(*self.organization).click()

    def click_general_info(self):
        self.driver.find_element(*self.general_info).click()
   
    def get_attribute_value(self, value):
        # return self.driver.find_element(*self.org_name).get_attribute(value)
        try:
            return self.driver.find_element(*self.add_user_password).get_attribute(value)
        except Exception as err:
            print("Sai nha....")
            traceback.print_exc()
            return 0


    



