# przełaczanie sie do nowej strony
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(r"C:\Users\slawek\PycharmProjects\czyst_selenium\drivers\chromedriver.exe")
# ...     Driver wykorzystany z uzyciem pliku w katalogu
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(r"C:\Users\slawek\Downloads\selenium_pliki\Test.html")
#driver.maximize_window()
#driver.find_element_by_xpath('//*[@id="newPage"]').click()
#driver.quit()   # zamyka wszystkie okna, metoda .close() zamyka okno na ktorej byl focus
#driver.close()
driver.find_element(By.ID, 'clickOnMe')
driver.find_element_by_xpath('//button[@id="newPage"]').click()

print(driver.title)
current_window_name = driver.current_window_handle
window_name = driver.window_handles
print(window_name)

for i in window_name:
    if i != current_window_name:
        driver.switch_to.window(i)

print(driver.title)
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]//div[1]//div[1]/input').send_keys("test")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]//div[1]//div[1]/input').send_keys(Keys.ENTER)

driver.switch_to.window(current_window_name)
print(driver.title)