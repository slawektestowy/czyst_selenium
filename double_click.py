from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\DoubleClick.html")
driver.maximize_window()


button = driver.find_element_by_xpath('//*[@id="bottom"]')

webdriver.ActionChains(driver).double_click(button).perform()   # kilkniecie dwukrotne