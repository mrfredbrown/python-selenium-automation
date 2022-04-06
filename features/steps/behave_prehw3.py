from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

#color_options = (by.css_selector, "#variation_color_name li");
color_options = (By.CSS_SELECTOR, '#variation_color_name li')
current_option = (By.CSS_SELECTOR, '#variation_color_name .a-row span')

@given('Open Amazon page')
def open_amazon(context):
    #context.driver = webdriver.Chrome(executable_path=b"C:\Users\Fred\Automation\python-selenium-automation\chromedriver.exe")

    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@given('Open Amazon product page')
def open_amazon(context):
    #context.driver = webdriver.Chrome(executable_path=b"C:\Users\Fred\Automation\python-selenium-automation\chromedriver.exe")

    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@given('Open Amazon homepage')
def open_amazon(context):
    #context.driver = webdriver.Chrome(executable_path=b"C:\Users\Fred\Automation\python-selenium-automation\chromedriver.exe")

    context.driver.get('https://www.amazon.com/')

@when('User types watches and submits')
def user_types_watches_and_submits(context):
    search_watch = context.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
    search_watch.clear()
    search_watch.send_keys('Watches')
    search_watch.submit()


@when('User adds watch to cart')
def add_watch_to_cart(context):
    sleep(8)
    watch = context.driver.find_element(By.XPATH, '//img[@src="https://m.media-amazon.com/images/I/71--0OOOpsL._AC_UL320_.jpg"]')
    watch.click()
    sleep(8)
    cart = context.driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]')
    cart.click()
    sleep(8)
    no = context.driver.find_element(By.XPATH, '//input[@aria-labelledby="attachSiNoCoverage-announce"]')
    no.click()



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

#    if (expect_result == empty):
#        print("test passed")
#    else:
#        print("test failed")

    assert expect_result == empty, f'Expected {expect_result}, but got {empty}'


@then('User verifies watch in cart')
def user_verifies_watch_in_cart(context):
    assert context.driver.find_element(By.XPATH, '//a[@aria-label="1 item in cart"]')
    print('there should only be 1 item in cart')
#     watch_cart = context.driver.find_element(By.TAG_NAME, 'h2').text
 #   print(empty)
 #   expect_result = "Your Amazon Cart is empty""

#    if (expect_result == empty):
#        print("test passed")
#    else:
#        print("test failed")

#    assert expect_result == empty, f'Expected {expect_result}, but got {empty}'


@then('Verify user can click through colors')
def user_can_click_colors(context):
    #assert context.driver.find_element(By.XPATH, '//a[@aria-label="1 item in cart"]')
    #print('there should only be 1 item in cart')
    expected_colors = ['Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Wash', 'Indigo Wash',\
                       'Light Blue Vintage', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash',\
                       'Rinsed', 'Vintage Wash', 'Washed Black', 'Bright White', 'Dark Khaki Brown',\
                       'Light Khaki Brown', 'Olive', 'Sage Green', 'Blue, Over Dye', 'Blue, Dip Dye']

    colors = context.driver.find_elements(*color_options)

    for color in colors:
        color.click()
        current = context.driver.find_element(*current_option).text
        assert current in expected_colors, f"{current} is not in expected color list"
        #print("color ")
