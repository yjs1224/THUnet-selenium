# THUnet-selenium
A tool to login THU net for your server

服务器连接清华校园网工具

使用selenium, python=3.8

默认使用Firefox

## 需要

pip install pyvirtualdisplay

sudo apt-get install Xvfb

## 在使用之前安装浏览器驱动

请按照本地浏览器版本下载对应驱动

wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz

tar -xvzf geckodriver-v0.23.0-linux64.tar.gz

chmod +x geckodriver

sudo mv geckodriver /usr/local/bin/


## 使用方法（examples）

仅连接校园网

python selenium_connect.py

定时， 自动连接校园网并自动登陆自己的清华邮箱给自己发一封本机ip的邮件

python selenium_connect.py --by_mail --timer 86400
