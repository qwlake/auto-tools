# -*- coding: utf-8 -*-
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def buy(driver, sleep_time=3):
    while True:
        try:
            driver.get("https://smartstore.naver.com/gonggami/products/4705579501")     # 페이지 열기
            # driver.get("https://smartstore.naver.com/hy_company/products/4594628495")   # 테스트
            body = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
            span_buy = body[0].find_element_by_class_name("buy")
        except Exception as e:
            print(f"{e}*** page load fail. wait {sleep_time}s *** \n")
            time.sleep(sleep_time)
            continue

        # 구매가능 여부 확인
        buy_button = span_buy.find_element_by_xpath("child::*")
        if buy_button.tag_name != "a":
            print(f"*** buying button not clickable. wait {sleep_time}s *** \n")
            time.sleep(sleep_time)
            continue

        # # 옵션 선택
        # select_list = driver.find_element_by_class_name("selectbox-source")
        # select_list_size = len(select_list.find_elements_by_tag_name("option"))
        # select = Select(select_list)
        # select.select_by_index(select_list_size-1)

        # 구매하기
        buy_button.click()

        # 창 전환 대기
        general_payments = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//label[@for='generalPayments']")))

        # 결제정보 선택 - '나중에결제'
        general_payments.click()
        pay18 = driver.find_element_by_xpath("//label[@for='pay18']")
        pay18.click()

        # 동의하기
        all_agree = driver.find_element_by_id("allAgree")
        all_agree.click()

        # 주문하기
        txt_order = driver.find_element_by_class_name("txt_order")
        txt_order.click()

        break
        
if __name__ == '__main__':
    ### Before Start ###
    # 1. open cmd.exe
    # 2. move to "C:\Program Files (x86)\Google\Chrome\Application"
    # 3. run "chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Temp/chromedriver""

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(executable_path="../chromedrivers/chromedriver80.exe", options=chrome_options)

    buy(driver, 5)