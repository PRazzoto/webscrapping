from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd


def webScrapper():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    url = "http://bianca.com"
    driver.get(url)

    title = driver.title
    h1_text = driver.find_element(By.TAG_NAME, "h1").text
    print("Title: " + title + "\nh1_text: " + h1_text)


if __name__ == "__main__":
    webScrapper()
