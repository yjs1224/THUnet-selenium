from selenium import webdriver
import time
import argparse

def login(username, passwd):
    driver = webdriver.Firefox()
    driver.get("http://net.tsinghua.edu.cn/")
    time.sleep(5)
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

def remote_login(username, passwd):
    # sudo apt install Xvfb
    # pip install pyvirtualdisplay
    import pyvirtualdisplay
    display = pyvirtualdisplay.Display(visible=0)
    display.start()
    driver = webdriver.Firefox()
    driver.get("http://net.tsinghua.edu.cn/")
    time.sleep(5)
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="selenium firefox")
    parser.add_argument("--user", required=True, type=str)
    parser.add_argument("--passwd", required=True, type=str)
    parser.add_argument("--is_remote", default="no", type=str, help="input yes or no (default no)")
    args = parser.parse_args()
    # driver = webdriver.Firefox()
    #
    # driver.get("http://net.tsinghua.edu.cn/")

    username = args.user
    passwd = args.passwd
    is_remote = args.is_remote
    if is_remote == "no":
        login(username=username,passwd=passwd)
    else:
        remote_login(username=username, passwd=passwd)
