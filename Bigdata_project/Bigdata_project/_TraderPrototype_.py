class _TraderPrototype_(object):
	
	def __init__(self, pair_info, date_range):
		'''
		parameter:
			pair_info: dict i.e. {"600001, 600002": (1, 2, 3, 4)}
			
			date_range: tuple i.e. ("2016-12-06 09:00:00", "2016-12-07 09:00:00")
		'''		
		self.name, self.up_in, self.up_out, self.down_in, self.down_out = pair_info.key, pair_info.values
		self.start, self.end = date_range
	
	def _trade(self):
		'''从价格数据库中获取指定日期范围内的数据进行回测，如果到期手中还有股票则按照最后一个交易日的价格强行卖出
		return:
			DataFrame:
				columns = ["time", "trade_num_1", "trade_price_1", "trade_num_2", "trade_price_2", "profit", "trade_type"]
		'''		
		