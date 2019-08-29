from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Test.html")
driver.maximize_window()

field = driver.find_element_by_xpath('//*[@value="Mickey"]')
field.clear()
field.send_keys("Test")