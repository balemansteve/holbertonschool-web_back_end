#!/usr/bin/env python3
"""
This module provides a function to update the 'topics' field
of all documents in a MongoDB collection that match a given 'name'.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all documents in the collection where the 'name' field matches
    the provided name by setting a new list of 'topics'.
    Parameters:
    - mongo_collection: pymongo collection object.
    - name (str): The name of the school to match.
    - topics (list): The list of topics to assign to the matched documents.
    Returns:
    None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
