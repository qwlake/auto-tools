# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="*")
html = driver.page_source

driver.get("http://everytime.co.kr")
driver.find_element_by_class_name("login").click()
driver.find_element_by_name("userid").send_keys("*")
driver.find_element_by_name("password").send_keys("*")
driver.find_element_by_class_name("submit").find_element_by_tag_name("input").click()

driver.find_element_by_class_name("mycommentarticle").click()
article_list = driver.find_elements_by_class_name("article")

for article in article_list:
    article.send_keys(Keys.CONTROL + "\n")
    driver.switch_to.window(driver.window_handles[-1])
    
    


driver.switch_to.frame("Main")
driver.find_element_by_id("USER_ID").send_keys('*')
driver.find_element_by_id("PWD").send_keys('*')
driver.find_element_by_id("button_login").ckick()

driver.switch_to.frame("top")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "top"))
)
driver.find_element_by_id("menu3").click()

driver.switch_to.parent_frame()
driver.switch_to.frame("main")

# search
#driver.find_element_by_id("txt_gwamok").send_keys('사회봉사')
#driver.find_element_by_id("btn_searchGwamok").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gawmok_list"))
)
gawmok_list = driver.find_elements_by_id("gawmok_list")

for gawmok in gawmok_list:
    bt = gawmok.find_element_by_tag_name("input")
    bt.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
