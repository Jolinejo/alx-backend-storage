#!/usr/bin/env python3
""" insert """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection """
    id_ = mongo_collection.insert_one(kwargs)
    return id_.inserted_id
