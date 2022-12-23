
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Open browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# Go to webpage
driver.get("https://clicktobuy.hyundai.co.in/#/bookACar")
driver.maximize_window()
time.sleep(2)

# select model
model_selector = driver.find_element(By.CSS_SELECTOR, "option[value='ZZ']")
model_selector.click()
time.sleep(2)

# select fuel type
fuel_locator = driver.find_element(By.CSS_SELECTOR, "option[value='U']")
fuel_locator.click()
time.sleep(2)

# select variant type
variant_locator = driver.find_element(By.CSS_SELECTOR, "option[value='3938']")
variant_locator.click()
time.sleep(2)

# select color
color_locator = driver.find_element(By.CSS_SELECTOR, "option[value='R4R']")
color_locator.click()
time.sleep(2)

# select interior color
int_color_locator = driver.find_element(By.CSS_SELECTOR, "option[value='NFB']")
int_color_locator.click()
time.sleep(2)

# select dealer state
dealer_locator = driver.find_element(By.CSS_SELECTOR, "option[value='TN']")
dealer_locator.click()
time.sleep(2)

# select dealer city
dealer_city_locator = driver.find_element(By.CSS_SELECTOR, "option[value='S10']")
dealer_city_locator.click()
time.sleep(2)

# select dealer
dealer_locator = driver.find_element(By.CSS_SELECTOR, "option[value='S1A04']")
dealer_locator.click()
time.sleep(2)

# click proceed
proceed_locator = driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']")
proceed_locator.click()
time.sleep(2)

# verify mobile number
proceed_locator = driver.find_element(By.XPATH, "//input[@id='mobileNumber']")
proceed_locator.send_keys("9999999999")
time.sleep(2)

# click verify
click_verify_locator = driver.find_element(By.XPATH, "//button[normalize-space()='Verify']")
click_verify_locator.click()
time.sleep(2)

# Verify page is redirected to OTP page
OTP_button_locator = driver.find_element(By.CSS_SELECTOR, ".pb-2.h6")
assert OTP_button_locator.is_displayed()

print("Book Car test completed successfully")
