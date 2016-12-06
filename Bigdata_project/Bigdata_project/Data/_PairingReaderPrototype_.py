class _PairingReaderPrototype_(object)_:

	def __init__(self):
		pass

	def read_pairs(self):
		'''读取配对结果
		return:
			a list of tuples of the code string of pairs, i.e.[('600001', '600002')...] 
		'''
		pass

	def save_cointegration(self, content):
		'''将协整结果存储到配对数据库中
		parameters:
			content: dict i.e. {"600001, 600002": 3.45}
		return: 
			bool 
				True: succeeded
				False: failed	
		'''
		pass
	
	def read_cointegration(self, content):
		'''读取协整结果
		parameters:
			content: string i.e. "600001, 600002"
		return:
			dict i.e. {"600001, 600002": 3.45}
		'''
		