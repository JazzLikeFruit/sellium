from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.coolblue.nl/winkelmandje?add=839184")
elem = driver.find_element_by_class_name("button--order")
elem.click()
assert "No results found." not in driver.page_source
driver.close()
