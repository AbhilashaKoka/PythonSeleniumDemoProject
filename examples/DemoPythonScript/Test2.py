from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the Bstack Demo website
driver.get("https://bstackdemo.com/")

# Find the sign-in button and click on it
signin_btn = driver.find_element(By.CSS_SELECTOR,"#signin")
signin_btn.click()

#Add implicit wait for element to be found
driver.implicitly_wait(10)

#Find the Username, Password and Login Button
username =driver.find_element(By.ID,"username")
password =driver.find_element(By.ID,"password")
login_btn= driver.find_element(By.ID,"login-btn")

#Select demouser as Username
username.click()
username_input= driver.find_element(By.CSS_SELECTOR,"#react-select-2-option-0-0")
username_input.click()

#Select testingisfun99 as Password
password.click()
password_input =driver.find_element(By.CSS_SELECTOR,"#react-select-3-option-0-0")
password_input.click()

# Submit the form
login_btn.click()
driver.implicitly_wait(10)

#Assert User is successfully Logged In
logout_btn= driver.find_element(By.CSS_SELECTOR,"#logout")
assert logout_btn.is_displayed()

#Closer the browser
driver.close()