from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#  webdriver
#def init_driver():
#    # ChromeDriverManager to manage the ChromeDriver installation
#    service = Service(ChromeDriverManager().install())
#    driver = webdriver.Chrome(service=service)
#    return driver

#def to_excel(df, name):
#    with pd.ExcelWriter(name + '.xlsx') as writer:
#        df.to_excel(writer, 'Sheet1')
#
#driver = init_driver()



def init_driver():
    try:
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        return driver
    except Exception as e:
        print(f"Error initializing ChromeDriver: {e}")
        raise

def to_excel(df, name):
    with pd.ExcelWriter(name + '.xlsx') as writer:
        df.to_excel(writer, 'Sheet1')

if __name__ == "__main__":
    driver = init_driver()