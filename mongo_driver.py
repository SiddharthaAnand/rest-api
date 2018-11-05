# Connection Client for MongoDB.

import pymongo

'''
A client class which uses pymongo driver to connect to Mongo Atlas Free Tier Account.
'''

class MongoClientConnection(object):

	def __init__(self, database_name=None, collection=None, username=None, pwd=None, url=None):
		self.database = database_name
		self.collection = collection
		self.client = None
		self.username = username
		self.pwd = pwd
		self.url = url
		self.mongo_url = "mongodb://"+self.username+":" + self.pwd + url

	def create_connection(self, database, collection):
		self.client  = pymongo.MongoClient(self.mongo_url)
		self.db = self.client.test

	def read(self):
		for doc in self.db.testCollection.find():
			print doc

	def write(self, data=None):
		pass

	def write_many(self, data=None):
		pass

