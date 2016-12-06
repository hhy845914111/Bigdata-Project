from Data._PriceReader_ import _PriceReader_
from pandas import DataFrame

class _CointegrationPrototype_(object):

	def __init__(self):
		'''初始化两个价格数据为一个DataFrame，其中时间为index，需要对齐，column名为股票代码
		'''
		self.df = DataFrame()

	def _check(self):
		'''检查DataFrame中的两个股票是否协整
		return:
			是否协整和协整系数的tuple
			(bool, float)
		'''
