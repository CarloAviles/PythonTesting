from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com")
driver.find_element_by_css_selector("#username").send_keys("Rahul")

# Generatind css from ClassName
# tagname.className -(make sure there are no spaces in class name.Replace with .)
# ej: .password
driver.find_element_by_css_selector(".password").send_keys("shetty")
driver.find_element_by_css_selector(".password").clear()  # limpia el contenido

driver.find_element_by_link_text("¿Olvidó la contraseña?").click()

# Xpath a un link  //tagname[text()='Textp del link']
driver.find_element_by_xpath("//a[text()='Cancelar']").click()

# Creating Xpath and CSS by Traversing Tags (childs)
# xpath=    ParentTag/ChildTag
# ej:    //div[@id="usernamegroup"]/label
# CSS =     parentTag childTag
# ej:     div[id="usernamegroup"] label

# Creating Xpath con Parent Locator(De padre a hijo)
# Xpath/parent::tagName
# Ej: //form[@name='login']/div[1]/label # en este ejemplo como hay 3 hijos 'div' se indica cual tomar y
# despues se  selecciona el hijo label

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
