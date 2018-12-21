#! /usr/bin/python
# -*- coding=utf-8 -*-
# author 张强
from flask import Flask
from flask import render_template
from flask import request
from splder import getbdsg
import re


app = Flask(__name__)


@app.route("/")
#  首页yelowduck
def home():
    return render_template("index.html")


@app.route("/s")
#  搜索结果页面
def search():
    #  获取用户输入关键字
    keyword = request.args.get("wd")
    reg = re.match(r"^\s|\+*$|^&.*|^#.*", keyword)
    if reg:
        return render_template("index.html")
    pn = request.args.get("pn")
    headers = request.headers.get("User-Agent")
    #  myip = request.remote_addr()
    #  print(myip)
    txt = getbdsg(headers, keyword, pn)
    return txt


@app.route('/myblog')
#  博客页面
def blog():
    return render_template("deome.html")


# app.run(debug=True)
if __name__ == "__main__":
    # 调试模式
    app.run(debug=True, host="0.0.0.0",  port=8000)
