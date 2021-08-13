from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import os

# config
options = webdriver.ChromeOptions()
# options.add_argument("--kiosk")
options.add_argument('--start-maximized')
options.add_argument('--incognito')
options.add_argument('--disable_popup_blocking')

driver = webdriver.Chrome(options=options)


def visit():

    try:
        url = 'https://popcat.click/'
        driver.get(url)

    except TimeoutException:
        print('Error')
        sleep(3)
        driver.quie()


def click_on_cat():


    cat_element = 'div.cat-img'
    cat = driver.find_element(By.CSS_SELECTOR, cat_element)
    

    while True:
        cat.click()


if __name__ == "__main__":
    visit()
    click_on_cat()
