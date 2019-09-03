from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Test.html")
driver.maximize_window()

first_name_input =driver.find_element_by_xpath('//*[@id="fname"]')


if first_name_input.is_enabled():
    first_name_input.send_keys("BLAALA")
else:
    print("Element is disabled")