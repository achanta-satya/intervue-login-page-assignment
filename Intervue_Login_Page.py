from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.intervue.io/")
original_window = driver.current_window_handle
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(2)  
# Loop through all windows to find the new one
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
driver.find_element(By.XPATH, "(//div[@class='AccessAccount-ColoredButton-Text'][normalize-space()='Login'])[1]").click()
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(email)
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(3)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('k').key_up(Keys.CONTROL).perform()
time.sleep(5)

search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Type what you want to search for"]'))
)
search_box.send_keys("hello")

driver.find_element(By.CSS_SELECTOR, '.SearchThrough__PlaceholderText-sc-8f4vh4-0.fEvpzS').click()
time.sleep(3)

assert "Try out your first interview" in driver.page_source #verifying that we are in interviews apge

driver.find_element(By.XPATH, '//div[@class="ProfileHeader__UsernameWrap-sc-1gwp6c1-2 jRhmUi"]').click()
driver.find_element(By.XPATH, '//a[@class="Dropdown__DropdownItemLink-k60emx-2 hHnuKn"][5]').click()
driver.quit()