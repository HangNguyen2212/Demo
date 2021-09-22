from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")
URL = "https://www.phptravels.net/admin"

driver.maximize_window()
driver.get(URL)
driver.implicitly_wait(10)

txt_username = "//input[@name='email' and @type='text']"
txt_password = "//input[@type='password']"
btn_login = "//button[@type='submit']"
tab_account = "//a[@href='https://www.phptravels.net/admin/profile']"
verify_email = "//input[@type='email']"

#login page
driver.find_element_by_xpath(txt_username).send_keys("admin@phptravels.com")
driver.find_element_by_xpath(txt_password).send_keys("demoadmin")
driver.find_element_by_xpath(btn_login).click()

#Verify login correctly or not
driver.find_element_by_xpath(tab_account).click()
if (driver.find_element_by_xpath(verify_email).get_attribute('value') == "admin@phptravels.com"):
  print("Logged correctly!")
else:
  print("Logged incorrectly!")