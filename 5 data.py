#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def test():
    data = process_map('C:/Benben/UD032 mongoDB/Lesson_6/example 5.osm', True)
    pprint.pprint(data)

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
            
        if element.find("nd") is not None:     
            node["node_refs"]=[]
            for nd in element.findall("nd"):   
                node["node_refs"].append(nd.attrib['ref'])
    
        return node
    else:
        return None

if __name__ == "__main__":
    test()