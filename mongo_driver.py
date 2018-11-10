# Connection Client for MongoDB Database Server.
# @author: Siddhartha Anand

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
		try:
			self.client  = pymongo.MongoClient(self.mongo_url)
			self.db = self.client.test
			print "Connection created..."
		except Exception as e:
			print e

	'''
	Read contents of collection from the mongo db server.
	'''
	def read_all(self, sort=None):
		# Returns a Cursor to the collection in the database.
		try:
			if sort in ["author_name"]:
				self.cursor = self.db.testCollection.find().sort([(sort, pymongo.ASCENDING)])
			else:
				self.cursor = self.db.testCollection.find()
			print "cursor here------"

		except Exception as e:
			return e
		finally:
			self.client.close()

	'''
	Create a data in json format to be returned to the client.
	'''
	def create_json(self):
		data_cache = []
		for doc in self.cursor:
			single_data = {}
			for key in doc:
				if "_id" not in str(key):
					single_data[str(key)] = doc[key]
			data_cache.append(single_data)
		return data_cache

	def write(self, data=None):
		if data:
			try:
				status = self.db.testCollection.insert_one(data)
				if isinstance(status, pymongo.result.InsertOneResult):
					return "Successful Inserted document"
			except Exception as e:
				print e

	def write_many(self, data=None):
		pass

