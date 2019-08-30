from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
driver.maximize_window()


drag_item = driver.find_element_by_xpath('//*[@id="draggable"]')
drag_target = driver.find_element_by_xpath('//*[@id="droptarget"]')

webdriver.ActionChains(driver).drag_and_drop(drag_item, drag_target).perform()
