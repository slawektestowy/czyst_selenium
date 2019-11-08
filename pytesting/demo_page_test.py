import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_setup():
    #global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.com/")
    driver.maximize_window()
    driver.close()






#def testing():
    #assert driver.title == "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
