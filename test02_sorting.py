import test_cases
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@test_cases.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # Login ke SauceDemo
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    yield driver
    driver.quit()

# ✅ TC05: Sort by Name A-Z
def test_sort_name_az(driver):
    wait = WebDriverWait(driver, 10)
    sort_dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(sort_dropdown)

    select.select_by_value("az")
    time.sleep(2)

# ✅ TC06: Sort by Name Z-A
def test_sort_name_za(driver):
    wait = WebDriverWait(driver, 10)
    sort_dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(sort_dropdown)

    select.select_by_value("za")
    time.sleep(2)

# ✅ TC07: Sort by Price (low to high)
def test_sort_price_low_high(driver):
    wait = WebDriverWait(driver, 10)
    sort_dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(sort_dropdown)

    select.select_by_value("lohi")
    time.sleep(2)

# ✅ TC08: Sort by Price (high to low)
def test_sort_price_high_low(driver):
    wait = WebDriverWait(driver, 10)
    sort_dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(sort_dropdown)

    select.select_by_value("hilo")
    time.sleep(2)
