from datetime import datetime
from mongo_driver import MongoClientConnection
import json


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
AUTHORS = {
  "author_one": {
    "author_name": "Siddhartha Anand",
    "author_community": [
      "community 1",
      "community 2",
      "community 3",
      "community 4"
    ],
    "author_articles_published": [
      "Spanning tree-based fast community detection methods in social networks."
    ],
    "coauthors_name_list": [
      "Partha Basuchowdhuri",
      "Subhashis Majumder",
      "Riya Roy",
      "Sanjoy Kumar Saha",
      "Diksha Roy Srivastava"
    ]
  },
  "author_two": {
    "author_name": "Partha Basuchowdhuri",
    "author_community": [
      "community 1",
      "community 2",
      "community 3",
      "community 4"
    ],
    "author_articles_published": [
      "Spanning tree-based fast community detection methods in social networks."
    ],
    "coauthors_name_list": [
      "Siddhartha Anand",
      "Subhashis Majumder",
      "Riya Roy",
      "Sanjoy Kumar Saha",
      "Diksha Roy Srivastava"
    ]
  }
}


def get_author_information(author_name):
    """
    This method returns the information of the author if available;
    :return:    author information
    """
    for author in AUTHORS:
        if author_name == AUTHORS[author]["author_name"]:
            return AUTHORS[author]

    return "No such author exists"


# Create a handler for our read (GET) people
def get_list_of_authors():
    """
    This function responds to a request for /api/v1/author
    with the complete lists of authors

    :return:        sorted list of authors
    """
    query_controller = MongoClientConnection("test", "testConnection")
    query_controller.read_all()
    data_cache = query_controller.create_json()

    return data_cache


def sort_results(sort=None):
    query_controller = MongoClientConnection("test", "testConnection")
    query_controller.read_all(sort=sort)
    data_cache = query_controller.create_json()

    return data_cache
