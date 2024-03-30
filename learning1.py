#𝐓𝐞𝐬𝐭 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨: Develop an automation script that bypasses the Basic Browser Authentication Popup.
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\suraj\\Downloads\\chromedriver.exe")
#driver.get("https://the-internet.herokuapp.com/basic_auth")
username = "admin"
password = "admin"
URL = "https://" + username + ":" + password + "@" + "the-internet.herokuapp.com/basic_auth"

driver.get("https://the-internet.herokuapp.com/basic_auth")


