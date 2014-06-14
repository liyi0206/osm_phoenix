"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "C:/Benben/UD032 mongoDB/Lesson_6/example 4.osm"
expected = ["Street","Avenue","Boulevard","Drive","Court","Place","Square","Lane","Road","Trail","Parkway","Commons"]
mapping = {"St": "Street","St.": "Street"}# UPDATE THIS VARIABLE

def test():
    st_types = audit(OSMFILE)
    #assert len(st_types) == 3
    pprint.pprint(dict(st_types))
    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            
            #if name == "West Lexington St.":
            #    assert better_name == "West Lexington Street"
            #if name == "Baldwin Rd.":
            #    assert better_name == "Baldwin Road"

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:street":
                    street_name=tag.attrib['v']
                    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
                    m = street_type_re.search(street_name)
                    if m:
                        street_type = m.group()
                        print street_type
                        if street_type not in expected:
                            street_types[street_type].add(street_name)
    return street_types

def update_name(name, mapping):
    name=name.replace('Ave','Avenue')    
    name=name.replace('St.','Street')
    name=name.replace('Rd.','Road')
    return name


if __name__ == '__main__':
    test()