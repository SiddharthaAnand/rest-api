from datetime import datetime
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
    ],
    "some_more_author_key": []
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
    ],
    "some_more_author_key": []
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
def read_author():
    """
    This function responds to a request for /api/v1/author
    with the complete lists of authors

    :return:        sorted list of authors
    """
    # Create the list of authors from our data
    return AUTHORS

