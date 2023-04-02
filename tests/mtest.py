import allure
from captcha_solver import CaptchaSolver
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
import base64


def test_queue_1():
    browser = webdriver.Chrome()
    with allure.step("Open page"):
        browser.get("https://sarajevo.kdmid.ru/queue/orderinfo.aspx?id=9543&cd=75659481&ems=B5464E4E")
        time.sleep(10)

    with allure.step("Solve captcha"):
        img_base64 = browser.execute_script("""
            var ele = arguments[0];
            var cnv = document.createElement('canvas');
            cnv.width = 200; cnv.height = 50;
            cnv.getContext('2d').drawImage(ele, 0, 0);
            return cnv.toDataURL('image/jpeg').substring(22);    
            """, browser.find_element(By.ID, 'ctl00_MainContent_imgSecNum'))
        with open(r"image.jpg", 'wb') as f:
            f.write(base64.b64decode(img_base64))

        solver = CaptchaSolver('rucaptcha', api_key='e4e4375778ded67a719d06c664258746')
        raw_data = open('image.jpg', 'rb').read()
        result = solver.solve_captcha(raw_data)

        browser.find_element(By.ID, 'ctl00_MainContent_txtCode').send_keys(result)
        browser.find_element(By.ID, 'ctl00_MainContent_ButtonA').click()
        time.sleep(3)

    with allure.step("Open schedule"):
        browser.find_element(By.ID, 'ctl00_MainContent_ButtonB').click()
        time.sleep(3)

    with allure.step("Check is empty"):
        browser.find_element(By.XPATH, "//*[@id='center-panel']/h1[text()='СПИСОК ОЖИДАНИЯ']")
        browser.find_element(By.XPATH, "//*[@id='center-panel']/p[1] \
        [text()='В настоящий момент на интересующее Вас консульское действие в системе предварительной записи ']")
        browser.find_element(By.XPATH, "//*[@id='center-panel']/p[1]/b[text()='нет свободного времени.']")

def test_queue_2():
    browser = webdriver.Chrome()

    with allure.step("Open page"):
        browser.get("https://sarajevo.kdmid.ru/queue/orderinfo.aspx?id=8004&cd=c604be16&ems=3C1E46ED")
        time.sleep(10)

    with allure.step("Solve captcha"):
        img_base64 = browser.execute_script("""
            var ele = arguments[0];
            var cnv = document.createElement('canvas');
            cnv.width = 200; cnv.height = 50;
            cnv.getContext('2d').drawImage(ele, 0, 0);
            return cnv.toDataURL('image/jpeg').substring(22);    
            """, browser.find_element(By.ID, 'ctl00_MainContent_imgSecNum'))
        with open(r"image.jpg", 'wb') as f:
            f.write(base64.b64decode(img_base64))

        solver = CaptchaSolver('rucaptcha', api_key='e4e4375778ded67a719d06c664258746')
        raw_data = open('image.jpg', 'rb').read()
        result = solver.solve_captcha(raw_data)

        browser.find_element(By.ID, 'ctl00_MainContent_txtCode').send_keys(result)
        browser.find_element(By.ID, 'ctl00_MainContent_ButtonA').click()
        time.sleep(3)

    with allure.step("Open schedule"):
        browser.find_element(By.ID, 'ctl00_MainContent_ButtonB').click()
        time.sleep(3)

    with allure.step("Check is empty"):
        browser.find_element(By.XPATH, "//*[@id='center-panel']/h1[text()='СПИСОК ОЖИДАНИЯ']")
        browser.find_element(By.XPATH, "//*[@id='center-panel']/p[1] \
        [text()='В настоящий момент на интересующее Вас консульское действие в системе предварительной записи ']")
        browser.find_element(By.XPATH, "//*[@id='center-panel']/p[1]/b[text()='нет свободного времени.']")





