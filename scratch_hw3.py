#css selectors

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=b"/chromedriver.exe")

driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

##amazon logo javascript test console command ($$("i.a-icon.a-icon-logo")
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

##Create account $$("h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")

##your name
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

#email $$("input#ap_email")
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

#password $$("input#ap_password")
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

#password check ap_password_check
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

#continue
driver.find_element(By.CSS_SELECTOR, "input#continue")

#Conditions of Use $$("a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Sign-In $$("input[type='metadata1']")
driver.find_element(By.CSS_SELECTOR, "input[type='metadata1']")


