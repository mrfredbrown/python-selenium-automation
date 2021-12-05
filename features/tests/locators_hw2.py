from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path=b"C:\Users\Fred\Automation\python-selenium-automation\chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
sleep(20)

search = driver.find_element(By.ID,'helpsearch')

search.clear()

search.send_keys('Cancel Order')

sleep(20)

search.submit()

sleep(20)
#driver.find_element(By.TAG_NAME, "h1")
#driver.find_element(By.Xpath, "//h1[contains(text(), 'Cancel Item or Orders']")
#message = driver.find_elements_by_tag_name('h2')[0].text

element = driver.find_element(By.TAG_NAME, 'h1').text
print(element)

#actual_result = driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/gp/help/customer/display.html?ref_=help_search_1-1&nodeId=GSL37WQTJZUYA9QE&qid=1638676093228&sr=1-1']").text
expected_result = "Cancel Items or Orders"

if (expected_result == element):
    print("test passed")
else:
    print("test failed")
#message = driver.find_element(By.Tag_Name, 'h1')[0].text
#if (message == "Cancel Item or Orders"):
#    print("Test Passed")
#else:
 #   print("Test Failed")
#actual_result = driver.find_element(By.XPATH, "//p[@class='a-color-secondary']").text



""""
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec


# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')
"""
driver.quit()
