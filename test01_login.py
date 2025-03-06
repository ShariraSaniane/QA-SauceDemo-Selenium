# login_test.py
from selenium.webdriver.common.by import By
import time
from webdriver_setup import get_driver

def test_login_success():
    """TC01: Login with valid credentials"""
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    assert "inventory.html" in driver.current_url, "❌ Login gagal!"
    print("✅ Login berhasil!")
    driver.quit()

def test_login_invalid():
    """TC02: Login with invalid credentials"""
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standardMe")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in error_message, "❌ Username and password do not match"
    print("✅ Username and password do not match")
    driver.quit()


def test_login_without_username():
    """TC03: Login without username """
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Password is required" in error_message, "❌ Password is required"
    print("✅ Password is required")
    driver.quit()

def test_login_without_Password():
    """TC04: Login without Password """
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username is required" in error_message, "❌ Username is required"
    print("✅ Username is required")
    driver.quit()



# Jalankan test case
test_login_success()
test_login_invalid()
test_login_without_username()
test_login_without_username()

