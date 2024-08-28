import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.test1
def test_case1():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    time.sleep(3)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    time.sleep(3)
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    time.sleep(3)
    text_box.send_keys("Selenium")
    time.sleep(3)
    submit_button.click()
    time.sleep(3)
    message = driver.find_element(by=By.ID, value="message")
    time.sleep(5)
    driver.quit()
