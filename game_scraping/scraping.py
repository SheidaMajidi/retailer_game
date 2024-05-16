from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#  webdriver
def init_driver():
    # ChromeDriverManager to manage the ChromeDriver installation
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def to_excel(df, name):
    with pd.ExcelWriter(name + '.xlsx') as writer:
        df.to_excel(writer, 'Sheet1')

driver = init_driver()
