#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if element.tag in ("node","way","relation"):
            user = element.attrib['user']
            #print user
            users.add(user)
    return users

def test():
    users = process_map('C:/Benben/UD032 mongoDB/Lesson_6/phoenix map.osm')
    print len(users)
    #pprint.pprint(users)
    #assert len(users) == 6

if __name__ == "__main__":
    test()