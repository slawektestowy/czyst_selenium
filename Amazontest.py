from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
driver.maximize_window()

# rozne metody lokalizacji elemntow
#driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]').click()
# driver.find_element_by_id('a-autoid-0-announce')
# driver.find_element_by_link_text('Shop now')

#driver.find_element_by_xpath('//*[@id="asin-shoveler-ns_4C58EYS6PYTZ7ZYJ6W5Q_2024_"]/div[2]//li[3]/span[1]//img')

a = driver.find_element_by_xpath('//*[@alt="Nintendo Switch - Neon Red and Neon Blue Joy-Con"]').get_attribute("src")
print(a)

# for i in driver.find_elements_by_id("img"):
#     print(i.src)
cv = (driver.find_elements_by_xpath('//link'))
print(type(cv))
b = len(driver.find_elements_by_xpath('//link'))  # ilosc elemenow link na stronie
print(b)

########

# Sprawdzenie czy obraz znajdue sie na stronie:
print(driver.find_element_by_xpath("//*[@alt='Cellphones']").get_attribute('naturalHeight'))