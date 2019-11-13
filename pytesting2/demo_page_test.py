import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time




@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(r"C:\selenium\selenium_pliki\chromedriver.exe")
#    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    driver.maximize_window()
    yield
    driver.close()






def testing(test_setup):
    assert driver.title == "Google"

def testing2(test_setup):
    assert driver.title == "Google"