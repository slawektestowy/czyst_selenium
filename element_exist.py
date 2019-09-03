from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\Test.html")
driver.maximize_window()

# element[s] zwraca liste elementów
paragraph = driver.find_elements_by_tag_name('p')

#print(len(paragraph))
z = len(paragraph)

if len(paragraph) > 0:
    print(f"Element is available {z} times")
else:
    print("No such element on site")

# II metoda znajdowanie elementu na stronie
try:
    driver.find_element_by_tag_name("papapa")
    print("Element is available")
except NoSuchElementException:
    print("No such element present on website")
