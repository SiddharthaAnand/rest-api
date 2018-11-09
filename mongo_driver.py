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
		self.mongo_url = "mongodb://{username}:{pwd}{url}".format(username=self.username, pwd=self.pwd, url=self.url)
		self.create_connection(self.database, self.collection)
		self.cursor = None

	def create_connection(self, database="test", collection="testCollection"):
		self.client  = pymongo.MongoClient(self.mongo_url)
		self.db = self.client.test
		print "Connection created..."

	def read_all(self):
		# Returns a Cursor to the collection in the database.
		self.cursor = self.db.testCollection.find()
		print "cursor here------"
		self.client.close()


	def create_json(self):
		data_cache = []
		single_data = {}
		for doc in self.cursor:
			single_data = {}
			for key in doc:
				if "_id" not in str(key):
					single_data[str(key)] = doc[key]
			data_cache.append(single_data)
		return data_cache

	def write(self, data=None):
		pass

	def write_many(self, data=None):
		pass

