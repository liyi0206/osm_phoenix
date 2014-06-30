#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
from pymongo import MongoClient

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        node["type"]=element.tag
        node["id"]=element.attrib['id']
        if 'visible' in element.attrib:
            node["visible"]=element.attrib['visible']
        if 'lat' in element.attrib and 'lon' in element.attrib:
            node["pos"]=[element.attrib['lat'],element.attrib['lon']]
        node["created"]={"version":element.attrib['version'],
                         "changeset":element.attrib['changeset'],
                         "timestamp":element.attrib['timestamp'],
                         "user":element.attrib['user'],
                         "uid":element.attrib['uid']}   
                         
        if element.find("tag") is not None: 
            node["address"]={"housenumber":"","street":""}
            for tag in element.findall("tag"):                
                if tag.attrib['k']=="addr:housenumber":
                    node["address"]["housenumber"]=tag.attrib['v']
                if tag.attrib['k']=="addr:street":  
                    node["address"]["street"]=tag.attrib['v']
                    
                if tag.attrib['k']=="amenity":  
                    node["amenity"]=tag.attrib['v']
                if tag.attrib['k']=="shop":  
                    node["shop"]=tag.attrib['v']
                if tag.attrib['k']=="leisure":  
                    node["leisure"]=tag.attrib['v'] 
                if tag.attrib['k']=="name":  
                    node["name"]=tag.attrib['v']
                                                          
                if tag.attrib['k']=="power":  
                    node["power"]=tag.attrib['v']                                
                if tag.attrib['k']=="cuisine":  
                    node["cuisine"]=tag.attrib['v']                    
                                                                            
                if tag.attrib['k']=="bicycle":  
                    node["bicycle"]=tag.attrib['v']                                
                if tag.attrib['k']=="foot":  
                    node["foot"]=tag.attrib['v'] 
                if tag.attrib['k']=="highway":  
                    node["highway"]=tag.attrib['v'] 
                                                                                                                                                                                                                                
        if element.find("nd") is not None:     
            node["node_refs"]=[]
            for nd in element.findall("nd"):   
                node["node_refs"].append(nd.attrib['ref'])
    
        return node
    else:
        return None

data = process_map('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm', True)

client = MongoClient('localhost:27017')
db = client.mydb
db.phoenix_osm.insert(data)

#db.phoenix.find_one()

### number of unique users
result0=db.phoenix.aggregate([{'$group':{'_id':"$created.user",'count':{'$sum':1}}}])
n_users=len(result0['result'])
pprint.pprint(n_users)

### number of nodes and ways
result1=db.phoenix.aggregate([{'$group':{'_id':"$type",'count':{'$sum':1}}}])
pprint.pprint(result1)

### number of each amenity,shop,leisure
result2=db.phoenix_osm.aggregate([{'$group':{'_id':"$amenity",'count':{'$sum':1}}},
                                  {"$match":{'_id':{'$ne':None}}},
                                  {'$sort': {'count':-1}},{"$limit":20}])
pprint.pprint(result2)
result3=db.phoenix_osm.aggregate([{'$group':{'_id':"$shop",'count':{'$sum':1}}},
                                  {"$match":{'_id':{'$ne':None}}},
                                  {'$sort': {'count':-1}},{"$limit":20}])
pprint.pprint(result3)
result4=db.phoenix_osm.aggregate([{'$group':{'_id':"$leisure",'count':{'$sum':1}}},
                                  {"$match":{'_id':{'$ne':None}}},
                                  {'$sort': {'count':-1}},{"$limit":10}])
pprint.pprint(result4)


