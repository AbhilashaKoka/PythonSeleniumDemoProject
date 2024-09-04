import time
from behave import given, when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging as logger

driver=webdriver.Chrome()
username="sita"
email="sita@gmail.com"
curraddr="adasffhlfhg"
peraddr="adsfsfafshf"

@given(u'User is on Landing Page')
def step_impl(context):
    driver.get("https://demoqa.com")
    print(driver.title)
    driver.implicitly_wait(1000)
    driver.execute_script('window.scrollBy(0, 300)')
    driver.find_element(By.XPATH,"//*[@class=\"category-cards\"]//following::div[@class=\"card-body\"]//h5[contains(text(),\"Elements\")]").click()
    driver.find_element(By.XPATH,"//*[@class=\"accordion\"]//div[@class=\"element-group\"]//following::span[@class=\"text\" and contains(text(),\"Text Box\")]").click()
    logger.info("User is on Element TextBox Landing Page")


@when(u'User enter details username, email, current address, permanent address')
def step_impl(context):
    driver.execute_script('window.scrollBy(0, 300)')
    driver.find_element(By.XPATH,"//*[@id='userName']").send_keys(username)
    driver.find_element(By.XPATH,"//*[@id='userEmail']").send_keys(email)
    driver.find_element(By.XPATH,"//*[@id='currentAddress']").send_keys(curraddr)
    driver.find_element(By.XPATH,"//*[@id='permanentAddress']").send_keys(peraddr)
    logger.info("User Enter Valid Details in InputFields")

@when(u'Click on Submit')
def step_impl(context):
    driver.find_element(By.XPATH,"//*[@id='submit']").submit()
    logger.info("User Submit Details")

@then(u'user should able to verify the detail on output area')
def step_impl(context):
    time.sleep(10)
    # elements=driver.find_elements(By.XPATH,"//*[@id=\"output\"]//p")
    # for menu in elements:
    # print(menu.text)
    logger.info("User Verify Details Successfully")



