#Este codigo es para hacer la prueba con Selenium el manipular un ventana de mensaje

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.find_element_by_css_selector("name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()