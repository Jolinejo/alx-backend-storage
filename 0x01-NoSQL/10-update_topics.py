#!/usr/bin/env python3
""" change topics """

import pymongo


def update_topics(mongo_collection, name, topics):
    """ update topics based on name """
    query = {"name": name}
    newval = {"$set": {"topics": topics}}
    db.mongo_collection.update_many(query, newval)
