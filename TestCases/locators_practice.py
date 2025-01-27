import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Option 1: Using driver.maximize_window()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")
# driver.find_element(By.XPATH,"//input[@name='EmailHomePage']").send_keys("naveen")
# driver.find_element(By.XPATH,"//input[@name='action_request']").click()
# time.sleep(5)
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
driver.execute_script("arguments[0].scrollIntoView(true);", button)
time.sleep(5)
# driver.quit()
