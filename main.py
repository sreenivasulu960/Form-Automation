from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# create an instance of microsoft edge
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert 'Python' in driver.title

# get the search box element
search_box = driver.find_element(By.NAME, 'q')
# clear the existing input like Search
search_box.clear()

# enter the search query
search_box.send_keys('pycon')
search_box.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
# close the browser
input("press Enter to close the browser")
driver.close()