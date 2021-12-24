from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    #context.driver = webdriver.Chrome(executable_path=b"C:\Users\Fred\Automation\python-selenium-automation\chromedriver.exe")

    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@given('Open Amazon homepage')
def open_amazon(context):
    #context.driver = webdriver.Chrome(executable_path=b"C:\Users\Fred\Automation\python-selenium-automation\chromedriver.exe")

    context.driver.get('https://www.amazon.com/')



@when('User types cancel order and submits')
def cancel_order(context):
    #sleep(20)
    search = context.driver.find_element(By.ID, 'helpsearch')

    search.clear()

    search.send_keys('Cancel Order')

    #sleep(20)
    search.submit()
    #sleep(5)

@when('User clicks on cart')
def clicks_on_cart(context):
    cart = context.driver.find_element(By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")
    cart.click()


@then('Verify cancel order page')
def verify_cancel_order_page(context):
    element = context.driver.find_element(By.TAG_NAME, 'h1').text
    print(element)
    expected_result = "Cancel Items or Orders"

    if (expected_result == element):
        print("test passed")
    else:
        print("test failed")


@then('Verify cart')
def verify_cart(context):
    empty = context.driver.find_element(By.TAG_NAME, 'h2').text
    print(empty)
    expect_result = "Your Amazon Cart is empty"

    if (expect_result == empty):
        print("test passed")
    else:
        print("test failed")


