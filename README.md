# THUnet-selenium
A tool to login THU net for your server

服务器连接清华校园网工具

使用selenium, python=3.8

默认使用Firefox

## 在使用之前安装浏览器驱动

请按照本地浏览器版本下载对应驱动

wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz

tar -xvzf geckodriver-v0.23.0-linux64.tar.gz

chmod +x geckodriver

sudo mv geckodriver /usr/local/bin/

## 如远程登陆需另外安装

sudo apt install Xvfb

pip install pyvirtualdisplay

## 使用方法

python selenium_connect.py --user yourusername --passwd yourpassword --is_remote yes

###  Notice : --is_remote 参数仅为yes or no

--is_remote yes: 本地使用

--is_remote no : 远程使用
