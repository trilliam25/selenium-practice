from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# click google search box and type search
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

# click on first link with specified text
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

# click on more
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "more"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "more")
link.click()

# close more popup
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "visibility-button"))
)
link = driver.find_element(By.ID, "visibility-button")
link.click()


print("Done!")
time.sleep(30)
driver.quit()
