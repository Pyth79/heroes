from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Firefox()
driver.get("https://www.hentaiheroes.com")
delay = 15
assert "Heroes" in driver.title
html = driver.page_source
time.sleep(5)
print(html)
# try:
#     elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="chat_block"]')))
#     print("Page is ready!")
# except TimeoutException:
#     print("Loading took too much time!")

# elem = driver.find_element(By.CSS_SELECTOR, 'button[id="popup_confirm"][class="blue_button_L"]')
# # elem.click()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source

# time.sleep(5)
driver.close()