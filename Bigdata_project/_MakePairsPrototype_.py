from pandas import DataFrame

class _MakePairsPrototype_(object):
	
	def __init__(self):
		'''确定配对寻找范围，默认从价格数据库中的汇总表获得
		'''
		self._range_df = DataFrame()

	def _make(self):
		'''尽可能将股票两两配对
		return: a list of tuple
			[("600001", "600002"), ...]
		'''
		pass
