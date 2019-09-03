from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Test.html")
driver.maximize_window()


paragraph = driver.find_element_by_tag_name('p')

if paragraph.is_displayed():
    print("Paragraph is displayed and you can see text")
    print(paragraph.text)
else:
    print("Element is hidden but you can see text as a get_attribute_textContent method")
    print(paragraph.get_attribute('textContent'))
