# Connection Client for MongoDB Database Server.

import pymongo
import read_credential

'''
A client class which uses pymongo driver to connect to Mongo Atlas Cloud Free Tier Account.
'''

class MongoClientConnection(object):

	def __init__(self, database_name=None, collection=None, username=None, pwd=None, url=None):

		self.database = database_name
		self.collection = collection
		self.client = None
		self.db = None
		self.username, self.pwd, self.url = read_credential.read_credential("credentials")
		self.mongo_url = "mongodb://"+self.username+":" + self.pwd + self.url
		self.create_connection(self.database, self.collection)
		print "url: ", self.mongo_url

	def create_connection(self, database="test", collection="testCollection"):
		self.client  = pymongo.MongoClient(self.mongo_url)
		self.db = self.client.test
		print "Connectionc created..."

	def read_all(self):
		# Returns a Cursor to the collection in the database.
		cursor = self.db.testCollection.find()
		print "cursor here------"
		data_cache = []
		for doc in self.db.testCollection.find():
			#data_cache.append(dict(doc))
			print doc
		self.client.close()
		return data_cache

	def write(self, data=None):
		pass

	def write_many(self, data=None):
		pass

