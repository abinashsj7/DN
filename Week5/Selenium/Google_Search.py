from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("Cognizant Digital Nurture")
search.send_keys(Keys.RETURN)

print(driver.title)

driver.quit()
