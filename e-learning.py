# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver.common.keys import Keys

class Learning():
    def __init__(self, id, pw, cource_name, section=0):
        driver = None
        if not driver:
            try:
                driver = webdriver.Chrome(executable_path="chromedriver78.exe")
            except:
                print("chromedriver78 fail")
        if not driver:
            try:
                driver = webdriver.Chrome(executable_path="chromedriver77.exe")
            except:
                print("chromedriver77 fail")
        if not driver:
            try:
                driver = webdriver.Chrome(executable_path="chromedriver76.exe")
            except:
                print("chromedriver76 fail")
        html = driver.page_source
        #soup = BeautifulSoup(html, "html.parser")
        self.id = id
        self.pw = pw
        self.driver = driver
        self.cource_name = cource_name
        self.section = section

    def learn(self):
        driver = self.driver
        driver.get("http://eruri.kangwon.ac.kr")    # 페이지 열기
        driver.find_element_by_id("username").send_keys(self.id)    # 로그인
        driver.find_element_by_id("password").send_keys(self.pw)
        driver.find_element_by_tag_name("Button").click()
        driver.implicitly_wait(2)
        close_notices = driver.find_elements_by_class_name("close_notice")
        for i in range(len(close_notices)): # 공지창 닫기
            close_notices[-i-1].click()
        courses = driver.find_elements_by_class_name("course_link") # 과목 목록 받아오기

        title_check = driver.find_elements_by_xpath("//div[@class='course-title']")
        for i, title in enumerate(title_check):
            temp = title.find_element_by_xpath("//h3")
            if self.cource_name in temp.text:
                courses[i].click()         # 과목 클릭
                break

        if self.section == 0:    # 현재 주차 강의 목록
            course_box_current = driver.find_elements_by_class_name("course_box_current")   # 현제 강의 목록 창 받기
            links = course_box_current[0].find_elements_by_tag_name("a")                    # 강의 목록 링크 저장
        else:   # 특정 주차 강의 목록
            links = driver.find_elements_by_xpath("//li[@id='section-" + self.section + "']//li[@class='activity vod modtype_vod ']//a[*]")  # n주차 강의 링크 목록

        for link in links:
            link.click()    # 강의 클릭

            # print("wait")
            # time.sleep(5)
            # print("wait complete")

            # webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

            # WebDriverWait(driver, 7).until(EC.alert_is_present()) # 팝업창 처리
            # driver.switch_to.alert.accept()

            driver.switch_to.window(driver.window_handles[-1])  # 오픈된 강의 창으로 포커스 이동
            
            while True: # 동영상 재생
                try:
                    driver.find_element_by_class_name("jw-state-playing")
                    break
                except:
                    driver.find_element_by_class_name("jw-video").click()
            while True: # 재생완료
                try:
                    driver.find_element_by_class_name("jw-state-complete")
                    break
                except:
                    pass
            driver.close()  # 동영상 창 닫기
            driver.switch_to.window(driver.window_handles[-1])  # 메인 창으로 포커스 이동

        driver.close()

if __name__ == '__main__':
    learn = Learning('학번', '비밀번호', '과목이름')
    learn.learn()