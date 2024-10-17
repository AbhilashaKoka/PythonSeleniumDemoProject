from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://bstackdemo.com/")
signin_btn = driver.find_element(By.CSS_SELECTOR,"#signin")
signin_btn.click()
driver.implicitly_wait(10)
username =driver.find_element(By.ID,"username")
password =driver.find_element(By.ID,"password")
login_btn= driver.find_element(By.ID,"login-btn")
username.click()
username_input= driver.find_element(By.CSS_SELECTOR,"#react-select-2-option-0-0")
username_input.click()
password.click()
password_input =driver.find_element(By.CSS_SELECTOR,"#react-select-3-option-0-0")
password_input.click()
login_btn.click()
driver.implicitly_wait(10)
logout_btn= driver.find_element(By.CSS_SELECTOR,"#logout")
assert logout_btn.is_displayed()
driver.close()