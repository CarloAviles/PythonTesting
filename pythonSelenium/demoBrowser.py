from selenium import webdriver

#driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver=webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
