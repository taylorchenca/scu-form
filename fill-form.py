import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://scu.az1.qualtrics.com/jfe/form/SV_0qc6GjIXqzBoom1")

name = ''
email = ''
phone = ''
wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.element_to_be_clickable((By.ID, "QID14-1-label"))).click()  # Click on "Student"
wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()  # Click on "Next"
wait.until(expected_conditions.element_to_be_clickable((By.ID, "QID1-6-label"))).click()  # Click on "No symptoms"
time.sleep(2)
wait.until(expected_conditions.element_to_be_clickable((By.ID, "QID8-5-label"))).click()  # Click on "No contact"
driver.find_element(By.ID, "QR~QID9").send_keys('N/A')  # Enter N/A
driver.find_element(By.ID, "QR~QID2").send_keys(name)  # Enter full name
wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()  # Click on "Next"

time.sleep(1)
driver.find_element(By.ID, "QR~QID3").send_keys(email)  # Enter email
wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()  # Click on "Next"

time.sleep(1)
driver.find_element(By.ID, "QR~QID7").send_keys(phone)  # Enter phone
wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()  # Click on "Next"

time.sleep(1)
wait.until(expected_conditions.element_to_be_clickable((By.ID, "QID20-3-label"))).click()  # Click on "housing@scu.edu"
wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()  # Click on "Next"

time.sleep(1)
wait.until(expected_conditions.element_to_be_clickable((By.ID, "QID22-1-label"))).click()  # Click on "I agree"
wait.until(expected_conditions.element_to_be_clickable((By.ID, "NextButton"))).click()  # Click on "Next"