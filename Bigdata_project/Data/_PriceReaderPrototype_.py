#数据获取接口

class _PriceReaderPrototype_(object):
	'''数据库的接口类
	'''
	
	def __init__(self):
		'''必要的初始化
		'''
		pass

	def update(self, share_code="all"):
		'''更新本地存储的股票数据
		parameters:
			optional:
				share_code: str
				股票编码的字符串或者"all"
			
		'''
		pass

	def read(self, share_code, start, end):
		'''读取本地的指定股票编码的数据
		parameters:
			share_code: str
			股票编码字符串
			
			optional:
				start: str
					"YYYY-MM-DD"
				end: str
					"YYYY-MM-DD"	
				若超过数据范围则返回尽可能大的区间
		'''
		pass

	def read_last(self, share_code, length):
		'''读取最近的几个数据
		parameters:
			share_code: str
				股票编码字符串
			length: int
				从后向前切片长度
		'''
		pass

	def get_summary(self):
		'''返回所有股票的信息
		return:
			pd.DataFrame: ["code": "600001", "name": "邯郸钢铁"]
		'''
		pass