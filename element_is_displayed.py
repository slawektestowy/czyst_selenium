from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Test.html")
driver.maximize_window()


paragrph = driver.find_element_by_tag_name('p')

if paragrph.is_displayed():
    print(paragrph.text)
else:
    print(paragrph.get_attribute('textContent'))
