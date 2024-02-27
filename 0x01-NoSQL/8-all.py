#!/usr/bin/env python3
""" 8-all """

import pymongo


def list_all(mongo_collection):
    """ print all """
    return list(mongo_collection.find({}))
