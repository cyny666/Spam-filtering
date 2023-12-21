import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from cnocr import CnOcr 
import re
import requests.utils
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import csv
name = ""
passwd = ""
data = []
def ocr_mail(path,title):
    global data
    mail_ocr = CnOcr()
    content = mail_ocr.ocr(path)
    # 用于存储高度大于90的元素的新列表
    filtered_data = []
    # 遍历每个元素，检查高度是否大于90
    for element in content:
            filtered_data.append(element['text'])
    mail_content = ''.join(filtered_data)
    # data的数据列表:题目、时间、发件人、
    data.append({
        '题目': title,
        '内容': mail_content

    })
    print(data)

def get_content():
    global data
    ocr = ddddocr.DdddOcr()
    driver = webdriver.Chrome()
    url = 'https://mail.sjtu.edu.cn/zimbra/mail#1'
    driver.get(url)
    time.sleep(2)
    id = {}
    driver.find_element(By.ID, "user").send_keys(name)
    driver.find_element(By.ID, "pass").send_keys(passwd)
    captcha = driver.find_element(By.ID, "captcha-img")
    with open('captcha.png', 'wb') as f:
        f.write(captcha.screenshot_as_png)
    with open('captcha.png', 'rb') as f:
        img_bytes = f.read()
    captcha = ocr.classification(img_bytes)
    driver.find_element(By.ID, "captcha").send_keys(captcha)
    time.sleep(1)
    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()
    time.sleep(2)
    driver.get("https://mail.sjtu.edu.cn/zimbra/mail#1")
    rubbish = driver.find_element(By.ID, "zti__main_Mail__4")
    rubbish.click()
    time.sleep(2)
    # 定义JavaScript脚本，将页面源代码返回给Python
    script = "return document.documentElement.outerHTML;"
    page_source = driver.execute_script(script)
    # 选择所有<li>元素
    li_elements = driver.find_elements(By.TAG_NAME, 'li')


    # 遍历每个<li>元素
    number = 1
    for li in li_elements:
        li.click()
        time.sleep(2)
        mail_content = driver.find_element(By.ID, "zv__TV-main__MSG__body")
        mail_content.screenshot("./imgs/test"+str(number)+".png")
        title = driver.find_element(By.XPATH,"/html/body/div[4]/div[10]/div[2]/div[1]/table/tbody/tr/td[2]/div/table[1]/tbody/tr/td[2]")
        ocr_mail("./imgs/test"+str(number)+".png",title.text)
        number += 1
        time.sleep(2)
    # 写入 CSV 文件
    with open("mail_content.csv", 'w', newline='', encoding='utf-8') as csv_file:
        # 创建 CSV 写入对象
        csv_writer = csv.writer(csv_file)

        # 写入表头
        csv_writer.writerow(['题目', '内容'])

        # 写入数据
        for item in data:
            csv_writer.writerow([item['题目'],item['内容']])

    print(f'数据已成功写入 CSV 文件: mail_content.csv')
    driver.quit()
    time.sleep(2)
