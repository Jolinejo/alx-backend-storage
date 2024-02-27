#!/usr/bin/env python3
""" list of school """


import pymongo


def schools_by_topic(mongo_collection, topic):
    """ schools by topic """

    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(schools)
