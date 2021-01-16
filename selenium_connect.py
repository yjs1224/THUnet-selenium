from selenium import webdriver
import time
import argparse
import os


def login(username, passwd):
    # sudo apt install Xvfb
    # pip install pyvirtualdisplay

    driver = webdriver.Firefox()
    driver.get("http://net.tsinghua.edu.cn/")
    time.sleep(1)
    if len(driver.find_elements_by_class_name("disconnect")) == 1:
        return
    try:
        input_username = driver.find_element_by_id("username")
        input_passwd = driver.find_element_by_id("password")
    except:
        input_username = driver.find_element_by_id("uname")
        input_passwd = driver.find_element_by_id("pass")
    input_username.send_keys(username)
    input_passwd.send_keys(passwd)
    submit = driver.find_element_by_name("connect")
    submit.click()

def login_timer(username,passwd, timer):
    os.system("ip addr > ./tmp.txt")
    time.sleep(1)
    with open("./tmp.txt", "r" ,encoding="utf-8") as f:
        text = f.read().split("\n")
    while True:
        Connecting = True
        while Connecting:
            try :
                login(username=username, passwd=passwd)
                Connecting = False
                print("time %s" % time.ctime())
                print("login!")
            except:
                print("time %s" % time.ctime())
                print("connecting failed")
        sending = True
        while sending:
            try:
                driver = webdriver.Firefox()
                driver.get("https://mails.tsinghua.edu.cn/")
                input_username = driver.find_element_by_name("uid")
                input_passwd = driver.find_element_by_name("password")
                input_username.send_keys(username)
                input_passwd.send_keys(passwd)
                submit = driver.find_element_by_class_name("loginbtn")
                time.sleep(1)
                submit.click()
                time.sleep(1)
                compose = driver.find_element_by_class_name("compose")
                compose.click()
                time.sleep(1)
                driver.switch_to.frame("compose1")
                # username+"@mails.tsinghua.edu.cn"
                time.sleep(1)
                input_receiver = driver.find_elements_by_class_name("inputElem")[0]
                input_receiver.send_keys(username + "@mails.tsinghua.edu.cn")
                send = driver.find_element_by_id("btnSend")
                time.sleep(1)
                driver.switch_to.frame("htmleditor")
                time.sleep(1)
                driver.switch_to.frame("HtmlEditor")
                time.sleep(1)
                input_context = driver.find_element_by_xpath("/html/body")
                input_context.click()
                input_context.send_keys(text)
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.switch_to.parent_frame()
                send.click()
                time.sleep(1)
                driver.switch_to.parent_frame()
                driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/div[3]/div/div[1]").click()
                sending = False
                print("time %s" % time.ctime())
                print("sendind successed")
            except:
                print("time %s"%time.ctime())
                print("sending failed")
        time.sleep(timer)
    # return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="selenium firefox")
    # parser.add_argument("--user", required=True, type=str)
    # parser.add_argument("--passwd", required=True, type=str)
    parser.add_argument("--by_mail", action="store_true")
    parser.add_argument("--timer", default=86400,type=int,help="send mail per timer(default 86400) seconds")
    username = input("input THUnet username : ")
    passwd = input("input your password : ")
    input("Pls Confirm your info Enter any key to begin, key CTRL+C to stop")
    os.system("clear")
    args = parser.parse_args()
    sending_email = args.by_mail
    timer = args.timer

    import pyvirtualdisplay
    display = pyvirtualdisplay.Display(visible=0)
    display.start()
    if not sending_email:
        login(username=username,passwd=passwd)
    else:
        login_timer(username=username,passwd=passwd,timer=timer)
