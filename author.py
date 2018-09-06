from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
AUTHOR = {
    "author_articles_published": [
        "Spanning tree-based fast community detection methods in social networks."
    ],
    "author_name": "Siddhartha Anand",
    "coauthor_communities_list": [
        "show coauthor community: group 1",
        "show coauthor community: group 1",
        "show coauthor community: group 1",
        "show coauthor community: group 1",
        "show coauthor community: group 1"
    ],
    "coauthors_name_list": [
        "Partha Basuchowdhuri",
        "Subhashis Majumder",
        "Riya Roy",
        "Sanjoy Kumar Saha",
        "Diksha Roy Srivastava"
    ]
}


# Create a handler for our read (GET) people
def read_author():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [AUTHOR[key] for key in sorted(AUTHOR.keys())]

