#𝐔𝐬𝐢𝐧𝐠 𝐬𝐞𝐥𝐞𝐧𝐢𝐮𝐦 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 - 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 𝐭𝐡𝐞 𝐠𝐫𝐨𝐰𝐢𝐧𝐠 𝐛𝐮𝐭𝐭𝐨𝐧 𝐚𝐧𝐝 𝐨𝐧𝐜𝐞 𝐜𝐥𝐢𝐜𝐤𝐞𝐝 𝐲𝐨𝐮 𝐬𝐡𝐨𝐮𝐥𝐝 𝐬𝐞𝐞 "𝐄𝐯𝐞𝐧𝐭 𝐓𝐫𝐢𝐠𝐠𝐞𝐫𝐞𝐝" 𝐦𝐞𝐬𝐬𝐚𝐠𝐞. 𝐕𝐞𝐫𝐢𝐟𝐲 𝐭𝐡𝐚𝐭 "𝐄𝐯𝐞𝐧𝐭 𝐓𝐫𝐢𝐠𝐠𝐞𝐫𝐞𝐝".
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\suraj\\Downloads\\chromedriver.exe")
driver.get("https://testpages.eviltester.com/styled/challenges/growing-clickable.html")
time.sleep(10)
#driver.find("//button[@ID='growbutton']").click()
button = driver.find_element(By.ID, "growbutton")
button.click()
txt = driver.find_element(By.ID, "growbuttonstatus").text
if txt == 'Event Triggered':
    print("pass")
else:
    print("fail")


driver.quit()