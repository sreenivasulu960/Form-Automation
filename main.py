from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e/')

print(driver.title)
