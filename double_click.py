from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#instalacja wind32.com    https://github.com/mhammond/pywin32/releases
import win32com.client as comclt



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r"D:\Selenium\czyste_sel\selenium_pliki\DoubleClick.html")
driver.maximize_window()


button = driver.find_element_by_xpath('//*[@id="bottom"]')

#webdriver.ActionChains(driver).double_click(button).perform()   # kilkniecie dwukrotne

#klikniecie PPM i wybór elementu z contextmenu
webdriver.ActionChains(driver).context_click(button).perform()
webdriver.ActionChains(driver).move_to_element(button).context_click().perform()
wsh= comclt.Dispatch("WScript.Shell")
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{DOWN}")