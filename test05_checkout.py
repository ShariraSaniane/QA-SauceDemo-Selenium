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

# ✅ TC13: Checkout Product with fill in your information
def test_Checkout_sucessfull(driver):
    wait = WebDriverWait(driver, 10)

    # Waiting for the product page to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # click button "Add to Cart"
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

    # Verify item added to cart
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Produk gagal ditambahkan ke keranjang"

    # Click the cart icon
    click_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
    click_cart.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_contents_container")))

    # Click the checkout button
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
    checkout_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_info_container")))

    # Input checkout information
    driver.find_element(By.ID, "first-name").send_keys("Sharira")
    driver.find_element(By.ID, "last-name").send_keys("Saniane")    
    driver.find_element(By.ID, "postal-code").send_keys("2023")

    # Click the Continue button
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn.btn_primary.cart_button.btn_action")
    checkout_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_summary_container")))

    # Click the Finish button 
    finish_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button")
    finish_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_complete_container")))
    time.sleep(2)

# ✅ TC14: Checkout Product without fill First Name 
def test_Checkout_without_fist_name(driver):
    wait = WebDriverWait(driver, 10)

    # Waiting for the product page to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # click button "Add to Cart"
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

    # Verify item added to cart
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Produk gagal ditambahkan ke keranjang"

    # Click the cart icon
    click_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
    click_cart.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_contents_container")))

    # Click the checkout button
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
    checkout_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_info_container")))

    # Input checkout information
    driver.find_element(By.ID, "first-name").send_keys("")
    driver.find_element(By.ID, "last-name").send_keys("Saniane")    
    driver.find_element(By.ID, "postal-code").send_keys("2023")

    # Click the Continue button
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn.btn_primary.cart_button.btn_action")
    checkout_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "First Name is required" in error_message, "❌ First Name is required"
    print("✅ First Name is required")
    driver.quit()


# ✅ TC14: Checkout Product without Last Name 
def test_Checkout_without_last_name(driver):
    wait = WebDriverWait(driver, 10)

    # Waiting for the product page to appear
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # click button "Add to Cart"
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

    # Verify item added to cart
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Produk gagal ditambahkan ke keranjang"

    # Click the cart icon
    click_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
    click_cart.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_contents_container")))

    # Click the checkout button
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
    checkout_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_info_container")))

    # Input checkout information
    driver.find_element(By.ID, "first-name").send_keys("sharira")
    driver.find_element(By.ID, "last-name").send_keys("")    
    driver.find_element(By.ID, "postal-code").send_keys("2023")

    # Click the Continue button
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn.btn_primary.cart_button.btn_action")
    checkout_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Last Name is required" in error_message, "❌ Last Name is required"
    print("✅ Last Name is required")
    driver.quit()

# ✅ TC14: Checkout Product without Postal Code  
def test_Checkout_without_postal_code(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    add_to_cart_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Produk gagal ditambahkan ke keranjang"

    click_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
    click_cart.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_contents_container")))

    checkout_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
    checkout_button.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_info_container")))

    driver.find_element(By.ID, "first-name").send_keys("Sharira")
    driver.find_element(By.ID, "last-name").send_keys("Saniane")    
    driver.find_element(By.ID, "postal-code").send_keys("")

    checkout_button = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn.btn_primary.cart_button.btn_action")
    checkout_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Postal Code is required" in error_message, "❌ Postal Code is required"
    print("✅ Postal Code is required")


