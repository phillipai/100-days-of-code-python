from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

chrome_driver_path = ("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value= '//*[@id="t-2073920312"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="t492665908"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')

email.send_keys(MY_EMAIL)
password.send_keys(MY_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

sleep(5)
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
