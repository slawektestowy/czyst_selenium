from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(r"C:\Users\slawek\PycharmProjects\pure_selenium\drivers\chromedriver.exe")
# ...     Driver wykorzystany z uzyciem pliku w katalogu
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.google.com")
driver.maximize_window()
