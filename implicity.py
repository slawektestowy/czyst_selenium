from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Waits2.html")
driver.maximize_window()


button = driver.find_element_by_xpath('//*[@id="clickOnMe"]')
button.click()
#time.sleep(5)
print(driver.find_element_by_tag_name("p").text)