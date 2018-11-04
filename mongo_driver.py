# Connection Client for MongoDB.

import pymongo


class MongoClientConnection(object):

	def __init__(self, db=None, collection=None):
		self.database = db
		self.collection = collection
		self.client = None
		self.username = "s_admin_13"
		self.pwd = "s_admin_13"
		self.mongo_url = "mongodb://"+self.username+":" + self.pwd + "@cluster0-shard-00-00-kvfhu.mongodb.net:27017,cluster0-shard-00-01-kvfhu.mongodb.net:27017,cluster0-shard-00-02-kvfhu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"

	def create_connection(self, database, collection):
		self.client  = pymongo.MongoClient(self.mongo_url)
		self.db = self.client.test

	def read(self):
		for doc in self.db.testCollection.find():
			print doc

	def write(self, data=None):
		pass