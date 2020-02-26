# -*- coding: utf-8 -*-
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# cashcheck_nums = ["010","0000","0000"]
def buy(driver, sleep_time=3, cashcheck_nums=[]):
    while True:
        # 페이지 열기 및 구매 가능 여부 확인
        try:
            driver.get("http://www.welkeepsmall.com/shop/shopdetail.html?branduid=951923")     # 페이지 열기
            # driver.get("http://www.welkeepsmall.com/shop/shopdetail.html?branduid=1000873")   # 테스트
            body = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
            btn_buy = body[0].find_element_by_class_name("btn_buy")
        except Exception as e:
            print(f"{e}*** page load fail. wait {sleep_time}s *** \n")
            time.sleep(sleep_time)
            continue

        # 옵션 선택
        select_option = driver.find_element_by_class_name("basic_option")
        select = Select(select_option)
        select.select_by_value("0")

        # 구매하기
        btn_buy.click()

        # 창 전환 대기
        general_payments = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//label[@for='generalPayments']")))

        # 배송지 정보, 적립금 셋팅
        driver.find_element_by_id("same").click()
        okreserve = driver.find_element_by_id("okreserve")
        driver.find_element_by_id("usereserve").send_keys(okreserve.get_attribute("value"))

        # 주문하기 클릭
        btn_foot = driver.find_element_by_class_name("btn-foot")
        btn_foot.find_element_by_tag_name("img").click()

        # 결제창 이동 및 팝업 닫기
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 7).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        
        # 결제방법 선택
        select_option = driver.find_element_by_tag_name("select")
        select = Select(select_option)
        select.select_by_value("06") # 국민은행 선택
        if len(cashcheck_nums) != 0:  # 현금영수증 신청시
            div_list = driver.find_elements_by_xpath("//td[@class='woong']/div")
            div_list[1].find_element_by_tag_name("input").click()
            cashcheck_div = driver.find_element_by_id("cash2")
            cashcheck_inputs = cashcheck_div.find_elements_by_tag_name("input")
            for c_input, c_num in zip(cashcheck_inputs, cashcheck_nums):
                c_input.send_keys(c_num)

        # 동의 및 결제하기
        orderbutton = driver.find_element_by_id("orderbutton")
        orderbutton.find_element_by_id("pay_agree").click()
        orderbutton.find_element_by_tag_name("img").click()

        break
        
if __name__ == '__main__':
    ### Before Start ###
    # 1. open cmd.exe
    # 2. move to "C:\Program Files (x86)\Google\Chrome\Application"
    # 3. run "chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/Temp/chromedriver""

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(executable_path="../chromedrivers/chromedriver80.exe", options=chrome_options)

    buy(driver, sleep_time=5, cashcheck_nums=[])