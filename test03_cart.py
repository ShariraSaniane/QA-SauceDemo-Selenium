import test_cases
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@test_cases.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    yield driver
    driver.quit()

# ✅ TC01: add product to chart
def test_add_product_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Produk gagal ditambahkan ke keranjang"

    time.sleep(2)

# ✅ TC02: Remove Product in product page
def test_remove_product_from_product_page(driver):
    wait = WebDriverWait(driver, 10)

    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()
    time.sleep(2)

    # Click "Remove" 
    remove_button = driver.find_element(By.CLASS_NAME, "btn_secondary")
    remove_button.click()

    time.sleep(2)
    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge") 
    assert len(cart_badge) == 0, "Produk gagal dihapus dari keranjang"
    
    time.sleep(2)  
