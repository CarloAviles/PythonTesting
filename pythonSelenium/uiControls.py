from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
#Para seleccionar todos los checkbox
for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()

#Para seleccionar solo un checkbox
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()

#Para seleccionar radiobuttons
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

