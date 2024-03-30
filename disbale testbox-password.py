# 𝐓𝐞𝐬𝐭 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨: Develop an automation script that will input a value in a disabled field (You cannot able to input value in field with sendkeys() directly if field is disabled)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\suraj\\Downloads\\chromedriver.exe")
driver.get("https://seleniumpractise.blogspot.com/2016/09/how-to-work-with-disable-textbox-or.html")

disabled_field = driver.find_element(By.ID, "pass")
driver.execute_script("arguments[0].removeAttribute('disabled')", disabled_field)
disabled_field.send_keys("testDisable")

driver.quit()

