from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon best seller webpage')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('User clicks on bestseller')
def clicks_bestseller(context):
    bestseller = context.driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
    bestseller.click()


@then('Verify bestseller page')
def bestseller_page(context):
    element_count = len(context.driver.find_elements(By.CSS_SELECTOR, "div#zg_header li"))
    amount = 5
    assert element_count == amount, f'Expected {amount}, but got {element_count}git