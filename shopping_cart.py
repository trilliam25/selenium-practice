from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://amazon.com")

number_of_items = 3
minimum_price = 40.00

# Wait for captcha
WebDriverWait(driver, 30).until_not(
        EC.presence_of_element_located((By.ID, "captchacharacters"))
    )
print("--------------------------------")
print("Captcha done!")
print("--------------------------------")

# Type text into search box
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)
input_element = driver.find_element(By.ID, "twotabsearchtextbox")
input_element.clear()
input_element.send_keys("bluetooth headphones" + Keys.ENTER)
print("--------------------------------")
print("Search done!")
print("--------------------------------")

# Add the items to the cart
for i in range(number_of_items):
    add_to_cart_id = "a-autoid-" + str(i + 1) + "-announce"
    print(add_to_cart_id)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, add_to_cart_id))
    )
    link = driver.find_element(By.ID, add_to_cart_id)
    link.click()
    try:
        link = driver.find_element(By.PARTIAL_LINK_TEXT, "Back to results")
        link.click()
        print("Cart item not added")
    except:
        print("Cart item added")
print("--------------------------------")
print("Add to cart done!")
print("--------------------------------")
time.sleep(3)

# Go to cart
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "nav-cart"))
)
link = driver.find_element(By.ID, "nav-cart")
driver.execute_script("arguments[0].scrollIntoView(true);", link)
try:
    link.click()
    print("Cart method 1")
except:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Go to Cart"))
    )
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Go to Cart")
    link.click()
    print("Cart method 2")
print("--------------------------------")
print("Go to cart done!")
print("--------------------------------")

# Remove all items
for i in range (number_of_items):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-price]"))
    )
    product_to_remove = driver.find_element(By.XPATH, "//div[@data-price]")
    print(f"product: {product_to_remove}")
    try:
        print("attempting to remove item...")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//button[@data-action='a-stepper-decrement']")
            )
        )
        button.click()
        print("Button clicked")
    except Exception as e:
        print(e)
    time.sleep(0.5)
print("--------------------------------")
print("Removing items done!")
print("--------------------------------")

print("Done!")
time.sleep(100)
driver.quit()
