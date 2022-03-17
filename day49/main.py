from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time

load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101174742&keywords=Analytic%20Recruiting%20Inc&location=Canada")

# Sign-in
driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]').click()
time.sleep(2)
email = driver.find_element(by=By.NAME, value="session_key")
email.send_keys(MY_EMAIL)
password = driver.find_element(by=By.NAME, value="session_password")
password.send_keys(MY_PASSWORD)
driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(10)

# Scan available jobs
jobs = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__title')
jobs_available = [job.text for job in jobs]
print(jobs_available)

# Select job posting and click on apply
while jobs_available:
    posting_num = 0
    try:
        driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply").click()
    except NoSuchElementException:
        posting_num += 1
        driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply").click()
    finally:
        # Complete application
        jobs_available.remove(jobs_available[posting_num])
        try:
            time.sleep(2)
            phone_num = driver.find_element(by=By.CLASS_NAME, value='fb-single-line-text__input')
            phone_num.clear()
            time.sleep(2)
            phone_num.send_keys(MY_PHONE_NUMBER)
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='footer button').click()
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Review your application"]').click()
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Submit application"]').click()
        except NoSuchElementException:
            print('Cannot apply, skipped')
    print("Work complete")
