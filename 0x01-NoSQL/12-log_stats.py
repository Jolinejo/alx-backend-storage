#!/usr/bin/env python3
""" some logs """

import pymongo


def log():
    """logging"""
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    logs = collection.count_documents({})

    print("{} logs".format(logs))
    print("Methods:")
    listi = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for elem in listi:
        num = collection.count_documents({"method": elem})
        print("\tmethod {}: {}".format(elem, num))

    stat = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(stat))


if __name__ == "__main__":
    log()
