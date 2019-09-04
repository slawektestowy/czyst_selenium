from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Test.html")
driver.maximize_window()


element_checkbox =driver.find_element_by_xpath('//*[@type="checkbox"]')


#element_checkbox.click()

if element_checkbox.is_selected():
    print("Wartosc byla zaznaczona, odznaczamy")
    element_checkbox.click()
else:
    print("Wartosc nie jest zaznaczona, klikniecie")
    element_checkbox.click()