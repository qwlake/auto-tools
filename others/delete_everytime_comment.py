# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="../chromedrivers/chromedriver80.exe")
html = driver.page_source
driver.get("http://everytime.co.kr")
driver.find_element_by_class_name("login").click()
driver.find_element_by_name("userid").send_keys("*")
driver.find_element_by_name("password").send_keys("*")
driver.find_element_by_class_name("submit").find_element_by_tag_name("input").click()
# driver.find_element_by_class_name("mycommentarticle").click()
driver.find_element_by_class_name("myarticle").click()
time.sleep(1)

article_links = []
while True:
    article_a_tag = driver.find_elements_by_xpath('//*[@id="container"]/div[2]/article/a')
    for article in article_a_tag:
        article_links.append(article.get_attribute('href'))
    try:
        driver.find_element_by_class_name('next').click()
    except:
        break

for article in article_links:
    driver.get(article)
    time.sleep(1)
    del_list = driver.find_elements_by_class_name('del')
    for d in del_list:
        d.click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
driver.close()