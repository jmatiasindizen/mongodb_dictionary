import unittest
from collection import Collection

class StoringTestCase(unittest.TestCase):
	
	def setUp(self):
		self.collection = Collection('mongodb://localhost', 'test_database', 'test_collection')
		for x in xrange(10):
			self.collection[x] = 'number - ' + str(x)
	
	def test_should_storeValue(self):
		self.assertEqual( "number - 5", self.collection[5] )
	
	def test_should_length_collection(self):
		self.assertEqual( 10, len(self.collection))

if __name__ == '__main__':
	collection = Collection('mongodb://localhost', 'test_database', 'test_collection')
	
	#find all documents
	for x in collection:
		print str(x) + str(type(x))
		
	#filter documents
	with collection({'_id':1}):
		for x in collection:
			print str(x) + str(type(x))
