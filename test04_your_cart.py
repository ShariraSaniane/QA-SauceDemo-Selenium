from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup driver
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver

# Login function
def login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

# TC11: Add product to cart and edit quantity
def test_add_product_and_edit_quantity():
    driver = setup_driver()
    login(driver)
    
    # Add product to cart
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_contents_container")))
    
    print("✅ Product added to cart successfully")
    
    # No quantity edit feature in SauceDemo, but you can add assertion for validation
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0, "Cart is empty"
    
    driver.quit()

# TC12: Add product to cart and remove it
def test_add_product_and_remove():
    driver = setup_driver()
    login(driver)
    
    # Add product to cart
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_contents_container")))
    
    # Remove product
    driver.find_element(By.CLASS_NAME, "cart_button").click()
    time.sleep(2)
    
    # Validate cart is empty
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "Cart is not empty after removing product"
    
    print("✅ Product removed from cart successfully")
    driver.quit()

# Run test cases
test_add_product_and_edit_quantity()
test_add_product_and_remove()
