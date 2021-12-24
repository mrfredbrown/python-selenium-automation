from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
#By ID Fred, can be commented out
driver.find_element(By.ID, 'twotabsearchtextbox')


#by xpath Fred

driver.find_element_by_xpath("//a[@href='/ref=nav_logo']")

driver.find_element_by_xpath("//span[@class='icp-nav-flag icp-nav-flag-us']")

# By XPATH
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//span[@class='icp-nav-flag icp-nav-flag-us']")

# By XPATH, multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")

# using contains for partial attr
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers') and @tabindex='0']")

# using text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sell') and @class='nav-a  ']") # partial text

# using multiple nodes:
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']/div[@id='nav-xshop']/a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//select[@id='searchDropdownBox']/option[@value='search-alias=audible']")

# using only tag
driver.find_element(By.XPATH, "//div")
# only attribute
driver.find_element(By.XPATH, "//*[@id='searchDropdownBox']/option[@value='search-alias=audible']")





