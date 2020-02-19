# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sugang():
    def __init__(self, id, pw):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.id = id
        self.pw = pw

    def start(self):
        while True:
            if self.click(self.driver) == 0:
                return 0
    
    def click(self, driver):
        driver.get("http://nsugang.kangwon.ac.kr")    # 페이지 열기
        html = driver.page_source
        
        driver.switch_to.frame("Main")
        driver.find_element_by_id("USER_ID").send_keys(self.id)    # 로그인
        driver.find_element_by_id("PWD").send_keys(self.pw)
        driver.find_element_by_id("button_login").click()
        
        driver.switch_to.frame("top")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "top"))
        )
        driver.find_element_by_id("menu3").click()  # 수강신청 탭 이동
        
        driver.switch_to.parent_frame()
        driver.switch_to.frame("main")
        
        # # search
        # driver.find_element_by_id("txt_gwamok").send_keys('사회봉사')
        # driver.find_element_by_id("btn_searchGwamok").click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "gawmok_list"))
        )
        gawmok_list = driver.find_elements_by_id("gawmok_list") # 과목 리스트 받기

        for gawmok in gawmok_list:
            try:
                bt = gawmok.find_element_by_tag_name("input")   # 신청 버튼 클릭
                bt.click()
            except:
                return -1;  # 신청 버튼 활성화 되지 않음
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
        return 0    # 정상적으로 종료
    
if __name__ == "__main__":
    sg = Sugang('학번', '비밀번호')
    sg.start()
