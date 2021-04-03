from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Carlos")
driver.find_element_by_css_selector("input[name='name']").send_keys("Carlos")
driver.find_element_by_name("email").send_keys("algo@algo.com")
driver.find_element_by_id("exampleCheck1").click()
#para buscar por CSS
#tagname[attribute='value'] --Tagname optional
#Ej: Input[name='name']
#Reg Ex: [attribute*='value']
#Ej: [class*='alert-success']

#Para generar la busqueda por CSS con ID
#tagname#ID -Tagname optional
#Ej:  input#username
#          #username    ##dado que el Tagname es opcional pero el ID obligatorio

#para buscar por xpath
# //tagname[@attribute=value] ---Tagname optional
#Ej: Input[@type='submit'
#Reg Ex: //*[contains(@attribute,'value')]
#Ej:  //*[contains(@class,'alert-success')]

# select class provide the method to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#Para el Select se ocupa la libreria selenium.webdriver.support.select
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()

#Imprimir el texto de exito
message = driver.find_element_by_class_name("alert-success").text

assert "success" in message