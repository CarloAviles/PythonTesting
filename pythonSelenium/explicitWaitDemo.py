# Using explicit wait
# A diferencia del modo implicito, esta forma se debe especificar el elemento poel que se va
# a esperar que aparezca, siendo este más eficiente que el Implicito que es global."
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
# Accediendo a través del padre para solo seleccionar los elementos de compra
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
print("linea 24")

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
print("linea 28")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
print("linea 31")
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print("linea 33")

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
#espera.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

print("linea 36")
print(driver.find_element_by_css_selector("span.promoInfo").text)
print("linea 38")
