#collection.py
import pymongo

	
class Collection(object):
	
	def __init__(self, connection_string, db_name, collection_name):
		self.connection = pymongo.MongoClient(connection_string)
		self.db = eval('self.connection.' + db_name + '.' + collection_name)
		self.find_expression = None

	def __enter__(self):
		pass
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass
		
	def __call__(self, search_expression):
		self.find_expression = search_expression
		return self
		
	def __iter__(self):
		if self.find_expression:
			self.cursor = self.db.find(self.find_expression)
		else:
			self.cursor = self.db.find()
		
		self.generator = self.generator_function()
		return self
	
	def __next__(self):
		return self.next()
	
	def generator_function (self):
		for element in self.cursor:
			yield element
	
	def next(self):
		try:
			return self.generator.next()
		except GeneratorExit:
			raise StopIteration()
		
	def __len__(self):
		return self.db.count()
		
	def __getitem__(self, key):
		return self.db.find_one({'_id': key})
		
	def __setitem__(self, key, value):
		if (type(value) == type({})):
			value.update({'_id': key})
		else:
			value = {'_id': key, 'value': value}
		try:
			self.db.insert(value)
		except pymongo.errors.DuplicateKeyError:
			print 'Error: Clave duplicada'
		
	def __delitem__(self, key):
		print '__delitem__'
		self.db.remove({'_id': key})
