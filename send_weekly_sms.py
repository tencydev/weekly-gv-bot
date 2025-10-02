import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 从 GitHub Secrets 读取账号密码
EMAIL = os.environ["GV_EMAIL"]
PASS = os.environ["GV_PASS"]

# 收件人号码列表（去掉括号和空格）
contacts = ["+18586333888", "+15732603230", "+18018108818", "+17609919966"]
message = "Hi！这是每周问候短信，祝你一周愉快！"

# 配置无头 Chromium
options = Options()
options.add_argument("--headless")  # 无头模式
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium-browser"  # 指定 Chromium 路径

driver = webdriver.Chrome(options=options)

try:
    # 打开 GV 登录页
    driver.get("https://voice.google.com/")
    time.sleep(3)

    # 登录
    driver.find_element(By.ID, "identifierId").send_keys(EMAIL)
    driver.find_element(By.ID, "identifierNext").click()
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys(PASS)
    driver.find_element(By.ID, "passwordNext").click()
    time.sleep(5)  # 等待登录完成

    # 循环发送短信
    for number in contacts:
        driver.get("https://voice.google.com/u/0/messages?itemId=new")
        time.sleep(3)

        # 填写收件人
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='To']").send_keys(number)
        time.sleep(1)

        # 填写短信内容
        driver.find_element(By.CSS_SELECTOR, "textarea").send_keys(message)
        time.sleep(1)

        # 点击发送
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Send']").click()
        print(f"已发送给 {number}")
        time.sleep(2)

finally:
    driver.quit()
