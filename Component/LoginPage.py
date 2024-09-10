from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_enter = (By.NAME, 'username')
        self.password_enter = (By.NAME, 'password')
        self.login_button = (By.XPATH,'//button[@type="submit"]')
    

        
    def email_input(self, email):
        self.driver.find_element(*self.username_enter).send_keys(email)

    def password_input(self, password):
        self.driver.find_element(*self.password_enter).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

   