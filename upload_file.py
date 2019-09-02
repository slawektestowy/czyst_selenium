from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\FileUpload.html")
driver.maximize_window()

input_on = driver.find_element_by_xpath('//*[@id="myFile"]')
path = os.path.abspath(r'D:\userdata\glibowsk\My Documents\!!!!!\selenium\selenium.txt')

input_on.send_keys(path)
