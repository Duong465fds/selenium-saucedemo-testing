import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    # Selenium Manager tự tìm/tải driver phù hợp nếu cần.
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()


def login(browser, username=VALID_USER, password=VALID_PASSWORD):
    browser.get(BASE_URL)
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()


def test_tc01_login_with_valid_credentials(driver):
    """TC01: Đăng nhập bằng tài khoản hợp lệ."""
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    assert "/inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"


def test_tc02_login_with_invalid_password(driver):
    """TC02: Đăng nhập bằng mật khẩu không hợp lệ."""
    login(driver, username=VALID_USER, password="wrong_password")
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert "Username and password do not match" in error.text


def test_tc03_products_list_is_displayed(driver):
    """TC03: Kiểm tra danh sách sản phẩm sau khi đăng nhập."""
    login(driver)
    products = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    assert len(products) == 6
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"


def test_tc04_add_product_to_cart(driver):
    """TC04: Thêm Sauce Labs Backpack vào giỏ hàng."""
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    assert cart_item.text == "Sauce Labs Backpack"


def test_tc05_logout(driver):
    """TC05: Đăng xuất và quay lại trang đăng nhập."""
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    assert driver.find_element(By.ID, "login-button").is_displayed()
    assert "saucedemo.com" in driver.current_url
