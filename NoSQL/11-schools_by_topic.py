#!/usr/bin/env python3
"""
This module provides a function to retrieve school documents from a MongoDB
collection that include a specific topic in their list of topics.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve all school documents that include the given topic.
    Parameters:
    - mongo_collection: pymongo collection object.
    - topic (str): The topic to search for within each document's 'topics' field.
    Returns:
    - list of documents (dict) where the 'topics' field contains the given topic.
    """
    return [i for i in mongo_collection.find() if topic in i.get('topics', [])]
