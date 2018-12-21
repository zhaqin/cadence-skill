#! /usr/bin/python
# -*- coding=utf-8 -*-
# author 张强

import requests
import re
# import string


def getbdsg(head, key, ye):
    # 增加请求头
    headers = {"User-Agent": "{}".format(head)}

    # 获取网页html
    res = requests.get("https://www.baidu.com/s?wd={}&pn={}&oq=python&tn=baiduhome_pg&ie=utf-8&rsv_idx=2&rsv_"
                       "pq=fd17328d0003b495&rsv_t=38dap%2BVHJ0mjJc2KIIOiZyUmXA%2B3xLzji%2Bwk4XzsDTlJ"
                       "jPhQVNIkTDdomNPS7pOGKB%2FW"
                       .format(key, ye), headers=headers).text

    html = res.replace('//www.baidu.com/img/baidu_jgylogo3.gif', 'static/img/unnamed.gif')

    html = html.replace('<span class="nums_text">百度为您找到相关结果',
                        '<span class="nums_text">Good为您找到相关结果')

    html = re.sub('<title>.[\s\S]*</title>', '<title>{}_Good搜索</title>'.format(key), html)

    html = html.replace('<input type="submit" id="su" value="百度一下" class="bg s_btn">',
                        '<input type="submit" id="su" value="Go" class="bg s_btn">')

    html = html.replace('</body>', '<script type="text/javascript">'
                        'var div = document.getElementById("content_right");div.remove();var '
                        'i = document.getElementsByClassName("c-icon c-icon-bear-p")[0].remove();var ii ='
                        'document.getElementsByClassName("c-icon c-icon-bear-pn");for(var a = 0; a<ii.length; a++)'
                        '{for(var i=0;i<1;i++){ii[a].remove();}}</script></body>')

    html = re.sub('<div[\s\S]id="u".[\s\S]*<div[\s\S]id="u1">', '<div id="u1">', html)

    return html


if __name__ == "__main__":
    # 默认使用googlechrome mac版进行网络爬虫
    googlechrome = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, "
                    "like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
    print(getbdsg(googlechrome, 'pythoon', '0'))
