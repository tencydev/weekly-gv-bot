import os
from googlevoice import Voice

def send_sms(number, message):
    voice = Voice()
    voice.login(email=os.environ["GV_EMAIL"], passwd=os.environ["GV_PASS"])
    voice.send_sms(number, message)
    print(f"已发送给 {number}: {message}")

if __name__ == "__main__":
    contacts = ["+1234567890", "+1987654321"]  # 联系人列表
    message = "Hi！这是每周的问候短信，祝你一周愉快！"

    for number in contacts:
        send_sms(number, message)
