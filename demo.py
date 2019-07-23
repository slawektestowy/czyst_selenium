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
#driver.find_element_by_id("fname").click()
driver.find_element_by_name('fname').click()
driver.find_element_by_link_text('IamWeirdLink')
driver.find_element_by_xpath('//*[@id="smileImage"]')
driver.find_element_by_class_name('topSecret')
print(driver.find_element_by_xpath('//*[@class="tableHeader" ][text()="Month"]').text)
driver.find_element_by_xpath('//*[@value="mercedes"]').click()
driver.find_element_by_xpath('//*[@value="male"]').click()
#driver.quit()

########### Obsluga alertow na stronnie

driver.find_element_by_xpath('//button[@id="clickOnMe"]').click()
driver.switch_to.alert.accept()
driver.find_element_by_xpath('//button[@id="clickOnMe"]').click()
driver.switch_to.alert.dismiss()

########  Wprowadzanie tekstu do elemntu na stronie
driver.find_element_by_xpath('//input[@id="fname"]').send_keys("Gonzo")

##### Wprowadzenie tesktu do elemntu i symulacja klawisze funkcyjnego po wpisaniu teego tekstu
driver.find_element_by_xpath('//input[@name="password"]').send_keys(Keys.ENTER)
driver.switch_to.alert.accept()  #### obsluga wyskakujacego okna
driver.switch_to.alert.dismiss()

### Wybieranie opcji z "selecta"
auto_selektor = Select(driver.find_element_by_xpath('//select'))
auto_selektor.select_by_index(2)


### Wypsianie tekstu z obiketu
aa = driver.find_element_by_xpath('//label[@for="fname"]').text
print(aa)
### Wypisanie tekstu z elementu ukrytego
print(driver.find_element_by_xpath('//p').get_attribute('textContent'))
### Wypisanie tekstu z elementu input(wprowadzonego przez webdrivera
print(driver.find_element_by_xpath('//input[@id="fname"]').get_attribute('value'))

### Sprawdzenie obecnosci obrazu na stronie
print(driver.find_element_by_xpath('//*[@id="smileImage"]').size.get('height'))
print(driver.find_element_by_xpath('//*[@id="smileImage"]').get_attribute('naturalHeight'))
                                                        # jesli wyniesie 0 to nie ma obrazka

