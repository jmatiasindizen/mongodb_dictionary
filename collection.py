import pymongo

class Collection(object):
	
	def __init__(self, connection_string, db_name, collection_name):
		self.connection = pymongo.MongoClient(connection_string)
		self.db = eval('self.connection.' + db_name + '.' + collection_name)
		self.cursor = self.db.find()
		self.generator = self.generator_function()
	
	def __iter__(self):
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
		return self.cursor.count()
		
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
		self.db.remove({'_id': key})
