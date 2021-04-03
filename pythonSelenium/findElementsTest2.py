import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
time.sleep(4)
#driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("label[for*='fromCity']").click()

#driver.find_element_by_class_name("appendBottom5").click()
#Ej: [class*='alert-success']
time.sleep(4)
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")

time.sleep(6)
cities = driver.find_elements_by_css_selector("p[class*='appendBottom5']")
print(len(cities))
for city in cities:
    print(city.text)
    if city.text == "Del Rio, United States":
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()

    #assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"