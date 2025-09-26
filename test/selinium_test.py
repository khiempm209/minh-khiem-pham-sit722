import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://_FRONTEND_API_"

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()

def test_create_customer(driver):
    driver.get(BASE_URL)
    form = driver.find_element(By.ID, "customer-form")
    assert form is not None, ("The website does not have the customer form")
    email = form.find_element(By.ID, "customer-email")
    password = form.find_element(By.ID, "customer-password")
    first_name = form.find_element(By.ID, "customer-first-name")
    last_name = form.find_element(By.ID, "customer-last-name")
    assert email is not None, ("The website does not have the email input in the customer form")
    assert password is not None, ("The website does not have the password input in the customer form")
    assert first_name is not None, ("The website does not have the first name input in the customer form")
    assert last_name is not None, ("The website does not have the last name input in the customer form")
    email.send_keys("test@example.com")
    password.send_keys("12345678")
    first_name.send_keys("Minh")
    last_name.send_keys("Pham")
    add_btn = form.find_element(By.XPATH, ".//button[normalize-space(.) = 'Add Customer']")
    assert add_btn is not None, ("The website does not have the button to submit a customer form")
    add_btn.click()
    time.sleep(3)
    customer_cards = driver.find_elements(By.CSS_SELECTOR, "#customer-list .customer-card")
    assert len(customer_cards) > 0, ("Cannot create a customer")

def test_create_product(driver):
    driver.get(BASE_URL)
    form = driver.find_element(By.ID, "product-form")
    assert form is not None, ("The website does not have the product form")
    product_name = form.find_element(By.ID, "product-name")
    product_price = form.find_element(By.ID, "product-price")
    product_stock = form.find_element(By.ID, "product-stock")
    assert product_name is not None, ("The website does not have the name input in the product form")
    assert product_price is not None, ("The website does not have the price input in the product form")
    assert product_stock is not None, ("The website does not have the stock input in the product form")
    product_name.send_keys("Item 1")
    product_price.send_keys(10)
    product_stock.send_keys(10)
    add_btn = form.find_element(By.XPATH, ".//button[normalize-space(.) = 'Add Product']")
    assert add_btn is not None, ("The website does not have the button to submit a product form")
    add_btn.click()
    time.sleep(3)
    product_cards = driver.find_elements(By.CSS_SELECTOR, "#product-list .product-card")
    assert len(product_cards) > 0, ("Cannot create a product")


