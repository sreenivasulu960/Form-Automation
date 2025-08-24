# Form Automation using Selenium

This is a simple project to automate form filling using Selenium. The project is written in Python.

## Current code(version 0.2)

```python
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
```

### Explanation

- The script opens a Chrome browser and navigates to the specified URL.
- It then finds the search box element using the `find_element` method and the `By.NAME` locator.
- The script clears any existing input in the search box using the `clear` method.
- It then enters the search query 'pycon' into the search box using the `send_keys` method.
- The script then presses the Enter key to submit the search query using the `Keys.RETURN` method.
- The script then asserts that the page source does not contain the text 'No results found.'.

## Prerequisites

- Python 3.8 or above
- Selenium
- ChromeDriverManager

## Installation

1. Clone the repository
2. Install the required packages using pip

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `main.py` script
2. The script will open a Chrome browser and navigate to the specified URL and close the browser and print the title
