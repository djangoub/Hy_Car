import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# Open browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# Go to webpage
driver.get("https://clicktobuy.hyundai.co.in/#/new-cars")
driver.maximize_window()
time.sleep(2)

# Quote click
quote_click_locator = driver.find_element(By.XPATH, "//button[normalize-space()='Get Quotation']")
quote_click_locator.click()
time.sleep(5)

#  Select Car Type
dropdown = Select(driver.find_element(By.XPATH, "//div/select"))
dropdown.select_by_value("V")
time.sleep(5)

# Chose Car
car_locator = driver.find_element(By.XPATH, "//div[contains(text(),'New Creta')]")
car_locator.click()
time.sleep(5)

# Enter mobile number
mobile_entry_locator = driver.find_element(By.XPATH, "//input[@id='mobileNumber']")
mobile_entry_locator.send_keys("9999999999")
time.sleep(3)

# Click verify button
click_verify_locator = driver.find_element(By.XPATH, "//button[normalize-space()='Verify']")
click_verify_locator.click()
time.sleep(5)

# To verify using Assert_Keyword
OTP_button_locator = driver.find_element(By.CSS_SELECTOR, ".pb-2.h6")
assert OTP_button_locator.is_displayed()

print("Home Page test completed successfully")
