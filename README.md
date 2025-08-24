# Form Automation using Selenium

This is a simple project to automate form filling using Selenium. The project is written in Python.

## Current code(version 0.1)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://towardsdatascience.com/automating-submission-forms-with-python-94459353b03e/')

print(driver.title)

```

The program will open a Chrome browser and navigate to the specified URL. It will then print the title of the page.

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
