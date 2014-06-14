#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
"""

Before you process the data and add it into MongoDB, you should
check the "k" value for each "<tag>" and see if they can be valid keys in MongoDB,
as well as see if there are any other potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data model
and expand the "addr:street" type of keys to a dictionary like this:{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with problematic characters.
Please complete the function 'key_type'.
"""
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    if element.tag == "tag":
        osm_k = element.attrib['k']
        print osm_k
        if lower.match(osm_k):
            keys['lower']+=1
        elif lower_colon.match(osm_k):
            keys['lower_colon'] +=1
        elif problemchars.match(osm_k):
            keys['problemchars'] +=1
        else:
            keys['other'] +=1     
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)
    return keys

def test():
    keys = process_map('C:/Benben/UD032 mongoDB/Lesson_6/example.osm')
    pprint.pprint(keys)
    #assert keys == {'lower': 5, 'lower_colon': 0, 'other': 2, 'problemchars': 0}

if __name__ == "__main__":
    test()