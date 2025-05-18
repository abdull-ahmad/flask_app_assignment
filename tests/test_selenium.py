from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5000/register")

driver.find_element(By.NAME, "username").send_keys("testuser")
driver.find_element(By.NAME, "password").send_keys("testpass")
driver.find_element(By.XPATH, "//button[text()='Register']").click()
time.sleep(1)

driver.get("http://localhost:5000/login")
driver.find_element(By.NAME, "username").send_keys("testuser")
driver.find_element(By.NAME, "password").send_keys("testpass")
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(2)

assert "testuser" in driver.page_source
driver.quit()