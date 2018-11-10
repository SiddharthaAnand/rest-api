from datetime import datetime
from mongo_driver import MongoClientConnection


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Get the author information based on author name
def get_author_information(author_name):
    """
    This method returns the information of the author if available;
    :return:    author information
    """
    query_controller = MongoClientConnection("test", "testConnection")
    query_controller.get_author(author_name)
    data_cache = query_controller.create_json()

    return data_cache


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


# Get the author list of names based on a sorting parameter
def sort_results(sort=None):
    query_controller = MongoClientConnection("test", "testConnection")
    query_controller.read_all(sort=sort)
    data_cache = query_controller.create_json()

    return data_cache
