#𝐔𝐬𝐢𝐧𝐠 𝐒𝐞𝐥𝐞𝐧𝐢𝐮𝐦 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐞𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐯𝐚𝐥𝐢𝐝 𝐜𝐨𝐝𝐞 𝐛𝐲 𝐤𝐞𝐲𝐛𝐨𝐚𝐫𝐝 𝐤𝐞𝐲𝐬 𝐛𝐲 𝐩𝐫𝐞𝐬𝐬𝐢𝐧𝐠 𝐭𝐡𝐞 𝐨𝐧𝐥𝐲 𝐤𝐞𝐲 𝐛𝐮𝐭𝐭𝐨𝐧 𝐚𝐧𝐝 𝐚𝐬𝐬𝐞𝐫𝐭𝐢𝐧𝐠 "𝐬𝐮𝐜𝐜𝐞𝐬𝐬" 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\suraj\\Downloads\\chromedriver.exe")

driver.implicitly_wait(15)
driver.maximize_window()
driver.get("https://qaplayground.dev/apps/verify-account/")
A = input("enter the no")
B = driver.find_elements_by_css_selector(".code-container input")
C = 0
for x in B:
    x.click()
    #time.sleep(0.5)
    x.send_keys(A[C])
    C = C+1 #when we want to add more value we can make the variable and it will change the value
D = driver.find_element_by_css_selector(".success").text
assert D.lower() == "success"
driver.quit()