from selenium import webdriver
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