#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.

The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    tags={'bounds': 0,'member':0,'nd':0,'node':0,
          'osm':0,'relation':0,'tag':0,'way':0}
    for event, elem in ET.iterparse(filename):
        if elem.tag == "bounds":
            tags["bounds"]=tags["bounds"]+1
        if elem.tag == "member":
            tags["member"]=tags["member"]+1
        if elem.tag == "nd":
            tags["nd"]=tags["nd"]+1
        if elem.tag == "node":
            tags["node"]=tags["node"]+1
        if elem.tag == "osm":
            tags["osm"]=tags["osm"]+1    
        if elem.tag == "relation":
            tags["relation"]=tags["relation"]+1         
        if elem.tag == "tag":
            tags["tag"]=tags["tag"]+1                                               
        if elem.tag == "way":
            tags["way"]=tags["way"]+1                                                                                  
                                                                                                                                                        
    return tags

def test():
    tags = count_tags('C:/Benben/UD032 mongoDB/Lesson_6/phoenix map.osm')
    pprint.pprint(tags)
    #assert tags == {'bounds': 1,'member': 3,'nd': 4,'node': 20,
    #                 'osm': 1,'relation': 1,'tag': 7,'way': 1}
   
if __name__ == "__main__":
    test()