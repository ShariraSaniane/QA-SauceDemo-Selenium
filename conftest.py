# import test_cases
# from selenium import webdriver

# @test_cases.fixture
# def login():
#     driver = webdriver.Chrome()
#     driver.get("https://www.saucedemo.com/")

#     # Login ke SauceDemo
#     driver.find_element("id", "user-name").send_keys("standard_user")
#     driver.find_element("id", "password").send_keys("secret_sauce")
#     driver.find_element("id", "login-button").click()

#     yield driver  # Mengembalikan driver setelah login
#     driver.quit()  # Menutup browser setelah test selesai
