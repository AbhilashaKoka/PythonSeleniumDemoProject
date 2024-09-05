from selenium import webdriver
from selenium.webdriver.common.by import By


class WebAutomation:

    def __init__(self):
         self.driver=webdriver.Chrome()

    def apply_wait(self):
        self.driver.implicitly_wait(10)

    def open_signup_page(self):
        self.driver.get("https://bstackdemo.com/")
        signin_btn = self.driver.find_element(By.CSS_SELECTOR,"#signin")
        signin_btn.click()

    def fill_username(self):
        username=self.driver.find_element(By.ID,"username")
        username.click()
        username_input= self.driver.find_element(By.CSS_SELECTOR,"#react-select-2-option-0-0")
        username_input.click()

    def fill_password(self):
        password =self.driver.find_element(By.ID,"password")
        password.click()
        password_input =self.driver.find_element(By.CSS_SELECTOR,"#react-select-3-option-0-0")
        password_input.click()

    def submit_form(self):
        login_btn= self.driver.find_element(By.ID,"login-btn")
        login_btn.click()

    def login_success(self):
        logout_btn= self.driver.find_element(By.CSS_SELECTOR,"#logout")
        assert logout_btn.is_displayed()
        self.driver.close()


b1 = WebAutomation()
b1.open_signup_page()
b1.apply_wait()
b1.fill_username()
b1.fill_password()
b1.submit_form()
b1.apply_wait()
b1.login_success()