from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Waits2.html")
driver.get(r"C:\Users\slawek\PycharmProjects\czyst_selenium\selenium_pliki\Waits2.html")
driver.maximize_window()
waiting = WebDriverWait(driver, 10, 0.5, )

button = driver.find_element_by_xpath('//*[@id="clickOnMe"]')
button.click()
waiting.until(lambda x: len(x.find_elements_by_tag_name("p")) == 1)
print(driver.find_element_by_tag_name("p").text)
