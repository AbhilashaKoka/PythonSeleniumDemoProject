from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

class WebAutomation:

    def __init__(self):

        self.driver = webdriver.Chrome()

    #Add implicit wait for element to be found

    def apply_wait(self):

        self.driver.implicitly_wait(10)

    # Navigate to Signup Page

    def open_signup_page(self):

        self.driver.get("https://bstackdemo.com/")

        signin_btn = self.driver.find_element(By.CSS_SELECTOR,"#signin")

        signin_btn.click()

    #Select demouser as Username

    def fill_username(self):

        username=self.driver.find_element(By.ID,"username")

        username.click()

        username_input= self.driver.find_element(By.CSS_SELECTOR,"#react-select-2-option-0-0")

        username_input.click()

    #Select testingisfun99 as Password

    def fill_password(self):

        password =self.driver.find_element(By.ID,"password")

        password.click()

        password_input =self.driver.find_element(By.CSS_SELECTOR,"#react-select-3-option-0-0")

        password_input.click()



    # Submit the form

    def submit_form(self):

        login_btn= self.driver.find_element(By.ID,"login-btn")

        login_btn.click()

    #Assert User is successfully Logged In

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