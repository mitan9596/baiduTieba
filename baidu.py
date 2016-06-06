# -*- coding: utf-8 -*-
import urllib.error
import urllib.request
import re
from tool import tool

# 百度贴吧爬虫类
class Baidu:
    
	# 初始化
    def __init__(self):
		# 传入所要爬取得贴吧地址
        self.baseURL = input('请输入你想要爬取的贴吧页面:')
		# 判断是否只看楼主
        judgement = input('是否只看楼主(y/n)')
        if judgement == 'y':
            seelz = 1
        else:
            seelz = 0
        self.seeLZ = '?see_lz='+str(seelz)+'&pn='
		# 默认爬取页面从第一页开始
        self.pageNum = 1
		# 执行main函数
        self.main()
    
	# 获取当前所在页的代码
    def getPage(self):
        try:
			# 构建URL
            url = self.baseURL + self.seeLZ + str(self.pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print(e.reason)
		# 返还utf-8格式的编码内容
		return pageCode
    
	# 获取帖子的标题
    def getTitle(self, pageCode):
		# 匹配帖子标题的正则表达式
        pattern = re.compile('<h\d class="core_title_txt.*?>(.*?)</h\d>')
		# 得到与之匹配的内容
        items = re.search(pattern,pageCode)
		# 判断items是否为空
        if items:
			# 输出得到的内容
            print(items.group(1))
        else:
            return None
    
	# 获取当前所在页
    def getPageNum(self, pageCode):
		# 匹配当前所在页的正则表达式
        pattern = re.compile('<span class="tP">(.*?)</span>')
		# 得到与之匹配的内容
        items = re.search(pattern, pageCode)
		# 判断items是否为空
        if items:
			# 输出得到的内容
            print('第'+items.group(1)+'页')
        else:
            return None        
    
	# 获取当前所在页的内容
    def getContent(self, pageCode):
		# 匹配当前所在页内的内容
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>')
		# 得到与之匹配的内容
        items = re.findall(pattern, pageCode)
		# 循环输出所得的内容
        for item in items:
            result = tool().change(item)
            print(result)
            
	# 获取帖子总页数
    def getAllPage(self):
		# 匹配总页数的正则表达式
        pattern = re.compile('<span class="red">(.*?)</span>')
		# 得到与之匹配的内容
        allpage = re.findall(pattern, self.getPage())
		# 将str转化为int
        page = int(allpage[0])
		# 循环爬取页面内容，直到当前所在页与总页数相等
        while self.pageNum <= page:
			# 执行函数getPage()获取新的url代码
            new_pagecode = self.getPage() 
			# 判断当前所在页是否为1，若为1执行函数getTitle()获取帖子标题,否则跳过
            if self.pageNum == 1:
                self.getTitle(new_pagecode)
            else:
                pass
			# 执行getContent()函数获取当前所在页内容
            self.getContent(new_pagecode) 
			# 进入下一个页面
            self.pageNum += 1

    def main(self):
        self.getAllPage()
        
Baidu()


