# -*- coding: utf-8 -*-
""" author Caiqm. """
import requests,random

class Express(object):
	"""docstring for Express"""
	def __init__(self, expressNum):
		super(Express, self).__init__()
		self.expressNum = expressNum

	# 获取快递信息函数
	def getExpressInfo(self, comCode):
		# 获取快递信息
		queryUrl = 'http://www.kuaidi100.com/query'
		temp = random.uniform(0, 1)
		queryRes = requests.get(queryUrl, params={'type': comCode, 'postid': self.expressNum, 'temp': temp})
		return queryRes

	# 获取快递信息主方法
	def main(self):
		# 通过订单号获取快递公司名称
		autoNumUrl = 'http://www.kuaidi100.com/autonumber/autoComNum'
		rsp = requests.get(autoNumUrl, params={'resultv2': 1, 'text': self.expressNum})
		comJson = rsp.json()
		# 获取快递公司编号
		for com in comJson['auto']:
			# 获取快递公司编号
			comCode = com['comCode']
			# 获取快递信息
			queryRes = self.getExpressInfo(comCode)
			# 格式json转化
			queryJson = queryRes.json()
			# 状态判断
			if queryJson['status'] == '200':
				# 循环输出快递信息
				for val in queryJson['data']:
					print("\n" + val['time'])
					print("\n" + val['context'])
				break
			else:
				print(queryJson['message'])

expressNum = input('请输入快递编号: ')
e = Express(expressNum)
e.main()