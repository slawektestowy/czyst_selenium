from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/")
driver.maximize_window()


element = driver.find_element_by_xpath('//*[@id="navbtn_tutorials"]')
webdriver.ActionChains(driver).move_to_element(element).perform()

#klikniecie na ten elemet z wykorzystaniem łańcucha 
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()