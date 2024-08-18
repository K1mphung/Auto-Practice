from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.login_menu = (By.XPATH, '//a[contains(text(),"Log in")]')
        self.register_button = (By.XPATH, '//button[contains(text(),"Register")]')
        self.gender = (By.XPATH, '//input[@id="gender-female"]')
        self.first_name_input = (By.XPATH, '//input[@id="FirstName"]')
        self.last_name_input = (By.XPATH, '//input[@id="LastName"]')
        self.day_select = (By.XPATH, '//select[@name="DateOfBirthDay"]')
        self.month_select = (By.XPATH,'//select[@name="DateOfBirthMonth"]')
        self.year_select = (By.XPATH,'//select[@name="DateOfBirthYear]')


        self.change_frame = (By.ID, 'cf-chl-widget-fsl2e')
        self.robot = (By.XPATH,'//span[contains(text(),"Verify you are human")]')
        
    def frame_switch(self):
        self.driver.find_element(*self.change_frame).switch_to.frame()
    
    def verify_human(self):
        self.driver.find_element(*self.robot).click()

    def enter_Login_page(self):
        self.driver.find_element(*self.login_menu).click()
        
    def enter_Register_page(self):
        self.driver.find_element(*self.register_button).click()

    def enter_Gender(self):
        self.driver.find_element(*self.gender).click()

    def enter_fist_name(self, firstname):
        self.driver.find_element(*self.first_name_input).send_keys(firstname)
   
    def enter_last_name(self, lastname):
        self.driver.find_element(*self.last_name_input).send_keys(lastname)

    def select_day(self, day):
        day_select = self.driver.find_element(*self.day_select)
        select = Select(day_select)
        select.select_by_value(day)

    def select_month(self, month):
        month_select = self.driver.find_element(*self.month_select)
        select = Select(month_select)
        select.select_by_value(month)

    def select_year(self, year):
        year_select = self.driver.find_element(*self.year_select)
        select = Select(year_select)
        select.select_by_value(year)
    

    



