from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\suraj\\Downloads\\chromedriver.exe")
driver.get("https://play1.automationcamp.ir/advanced.html")
driver.set_page_load_timeout(10)
text = driver.execute_script("return window.getComputedStyle(document.querySelector('.star-rating'),'::after').getPropertyValue('content')")
# Remove the quotes from the returned string
txt = text[1:-1]
driver.find_element_by_css_selector("#txt_rating").send_keys(txt)
driver.find_element_by_css_selector("#check_rating").click()
driver.quit()
