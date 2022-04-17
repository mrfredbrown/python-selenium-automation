from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait





@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')

@given('Open Amazon best seller webpage')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('User clicks on bestseller')
def clicks_bestseller(context):
    bestseller = context.driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
    bestseller.click()

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)



@when('Click on Amazon Privacy Notice link')
def click_on_privacy_notice(context):
    privacy_notice = context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']")
    privacy_notice.click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    #sleep(10)
    #context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
    context.driver.switch_to.window(current_windows[1])
    #pass


@then('Verify bestseller page')
def bestseller_page(context):
    element_count = len(context.driver.find_elements(By.CSS_SELECTOR, "div#zg_header li"))
    amount = 5
    assert element_count == amount, f'Expected {amount}, but got {element_count}'



@then('Verify Amazon Privacy Notice page is opened')
def amazon_privacy_page(context):
    #element_count = len(context.driver.find_elements(By.CSS_SELECTOR, "div#zg_header li"))
    #amount = 5
    text1 = 'Amazon.com Privacy Notice'
    #assert element_count == amount, f'Expected {amount}, but got {element_count}'
    #$x("//h1[text()='Amazon.com Privacy Notice']")
    context.driver.find_element(By.XPATH, "//h1[text()='Amazon.com Privacy Notice']")


    print("test passed")



@then('User can close new window and switch back to original')
def close_page(context):
    #element_count = len(context.driver.find_elements(By.CSS_SELECTOR, "div#zg_header li"))
    #amount = 5
    #context.driver.close()
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
