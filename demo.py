from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(r"C:\Users\slawek\PycharmProjects\czyst_selenium\drivers\chromedriver.exe")
# ...     Driver wykorzystany z uzyciem pliku w katalogu
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(r"C:\Users\slawek\Downloads\selenium_pliki\Test.html")
driver.maximize_window()
#driver.find_element_by_xpath('//*[@id="newPage"]').click()
#driver.quit()   # zamyka wszystkie okna, metoda .close() zamyka okno na ktorej byl focus
#driver.close()
driver.find_element(By.ID, 'clickOnMe')
#driver.find_element_by_id("fname").click()
driver.find_element_by_name('fname').click()
driver.find_element_by_link_text('IamWeirdLink')
driver.find_element_by_xpath('//*[@id="smileImage"]')
driver.find_element_by_class_name('topSecret')
print(driver.find_element_by_xpath('//*[@class="tableHeader" ][text()="Month"]').text)
driver.find_element_by_xpath('//*[@value="mercedes"]').click()
driver.find_element_by_xpath('//*[@value="male"]').click()
#driver.quit()