#Este codigo es para hacer la prueba con Selenium el manipular un ventana de mensaje
import time

from selenium import webdriver

validateText= "Option3"

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

driver.find_element_by_css_selector("#name").send_keys("Option3")

driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()
#Para dar en el boton de cancelar o negar
#alert.dismiss()