# import time
# from behave import given, when,then
# from selenium import webdriver
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
#
# @given(u'I am in from landing page')
# def step_impl(context):
#     driver.get("https://demoqa.com")
#     print(driver.title)
#     driver.execute_script('window.scrollBy(0, 300)')
#     driver.find_element(By.XPATH, "//*[@class=\"category-cards\"]//following::div[@class=\"card-body\"]//h5[contains(text(),\"Forms\")]").click()
#     driver.find_element(By.XPATH,"//*[@class=\"accordion\"]//div[@class=\"element-group\"]//following::span[@class=\"text\" and contains(text(),\"Practice Form\")]").click()
#     driver.execute_script('window.scrollBy(0, 300)')
#
#
# @when(u'I fill all valid credential and click on submit')
# def step_impl(context):
#     driver.find_element(By.XPATH,"//*[@id=\"firstName\"]").send_keys("sita",Keys.TAB)
#     driver.find_element(By.XPATH,"//*[@id=\"lastName\"]").send_keys("Kumari",Keys.TAB)
#     driver.find_element(By.XPATH,"//*[@id=\"userEmail\"]").send_keys("sitakumari@gmail.com",Keys.TAB)
#     driver.execute_script('window.scrollBy(0, 300)')
#     radio_button=driver.find_element(By.XPATH,"//*[@id=\"genterWrapper\"]//following::label[contains(text(),\"Male\")]//preceding-sibling::input[@name=\"gender\"]")
#     if radio_button.is_selected():
#         print("Radio Button is selected!!!")
#     else:
#         ActionChains(driver) \
#             .move_to_element(radio_button) \
#             .click().perform()
#         radio_button.send_keys(Keys.TAB)
#     driver.execute_script('window.scrollBy(0, 300)')
#     driver.find_element(By.XPATH, "//*[@id=\"userNumber\"]").send_keys("9142343241",Keys.TAB)
#     driver.find_element(By.XPATH, "//*[@id=\"dateOfBirthInput\"]").send_keys("28 JUN 1983",Keys.TAB, Keys.ENTER, Keys.TAB)
#     time.sleep(20)
#     driver.find_element(By.XPATH,"//div[@class=\"subjects-auto-complete__input\"]/input[@type=\"text\"]").send_keys("Computer Science",Keys.TAB, Keys.TAB)
#     driver.execute_script('window.scrollBy(0, 300)')
#     time.sleep(30)
#     hobbies_check_box=driver.find_element(By.XPATH,"//div[@id=\"hobbiesWrapper\"]//label[contains(text(),\"Reading\")]//preceding-sibling::input")
#     if hobbies_check_box.is_selected():
#         print("check box is selected!!!")
#     else:
#         ActionChains(driver) \
#             .move_to_element(hobbies_check_box) \
#             .click().perform()
#         hobbies_check_box.send_keys(Keys.TAB, Keys.TAB)
#     driver.find_element(By.XPATH,"//*[@id=\"uploadPicture\" and @type=\"file\"]").send_keys("D://Users//akoka//Downloads//sampleFile.jpeg",Keys.TAB)
#     driver.find_element(By.XPATH,"//textArea[@id=\"currentAddress\"]").send_keys("sadsaffhkfh",Keys.TAB)
#     driver.find_element(By.XPATH,"//input[@id=\"react-select-3-input\"]").send_keys("Uttar Pradesh",Keys.TAB)
#     driver.find_element(By.XPATH,"//*[@id=\"react-select-4-input\"]").send_keys("Lucknow",Keys.TAB)
#     driver.find_element(By.XPATH,"//*[@id=\"submit\"]").submit()
#
#
#
#
#
#
# @then(u'I am able to verify form details successfully')
# def step_impl(context):
#     print("Verify!!!")
# #      modal_box=driver.find_elements(By.XPATH,"//*[@class=\"modal-dialog modal-lg\"]")
# #      ActionChains(driver) \
# #     .move_to_element(modal_box) \
# #     .perform()
# # column=driver.find_elements(By.XPATH, "//table[@class=\"table table-dark table-striped table-bordered table-hover\"]/tbody/tr")
# # for rows in column:
# #      print( rows.driver.find_elements(By.XPATH,"td[1]").getAttribute("innerText"))
# #      print(rows.driver.find_elements(By.XPATH,"td[2]").getAttribute("innerText"))
# #
# #
# # modalCloseButton=driver.find_element(By.XPATH,"//*[@class=\"modal-dialog modal-lg\"]/div/div[3]/button[@type=\"button\"]")
# # ActionChains(driver) \
# #     .move_to_element(modalCloseButton) \
# #    .click().perform()
# #
# # modalCloseButton.sendKeys(Keys.ESCAPE)
# # driver.execute_script("window.scrollBy(0,-350)")
