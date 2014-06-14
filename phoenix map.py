import xml.etree.ElementTree as ET
import pprint
import re

### 2 number of unique users
def test():
    users = process_map('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm')
    print len(users)

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if element.tag in ("node","way","relation"):
            user = element.attrib['user']
            #print user
            users.add(user)
    return users

if __name__ == "__main__":
    test()
    
### 3 number of nodes and ways
def test():
    tags = count_tags('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm')
    pprint.pprint(tags)

def count_tags(filename):
    tags={'node':0,'way':0}
    for event, elem in ET.iterparse(filename):
        if elem.tag == "node":
            tags["node"]=tags["node"]+1                                              
        if elem.tag == "way":
            tags["way"]=tags["way"]+1                                                                                                                
    return tags
    
if __name__ == "__main__":
    test()
    
#### 4 number of cafes and shops
#def test():
#    counts = process_map('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm')
#    pprint.pprint(counts) 
#
#def process_map(filename):
#    counts = {"cafe":0,"restaurant":0,"fast_food":0,"fuel":0,
#              "supermarket":0,"greengrocer":0,"organic":0}
#    for _, element in ET.iterparse(filename):
#        if element.tag in ("tag"):
#            if element.attrib['v']=="cafe":
#                counts["cafe"]=counts["cafe"]+1
#            if element.attrib['v']=="restaurant":
#                counts["restaurant"]=counts["restaurant"]+1
#            if element.attrib['v']=="fast_food":
#                counts["fast_food"]=counts["fast_food"]+1
#            if element.attrib['v']=="fuel":
#                counts["fuel"]=counts["fuel"]+1
#                
#            if element.attrib['v']=="supermarket":
#                counts["supermarket"]=counts["supermarket"]+1
#            if element.attrib['v']=="greengrocer":
#                counts["greengrocer"]=counts["greengrocer"]+1   
#            if element.attrib['v']=="organic":
#                counts["organic"]=counts["organic"]+1    
#    
#    return counts
#
#if __name__ == "__main__":
#    test()



    
### 4 number of other types of nodes
def test():
    dct = process_map('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm')
    pprint.pprint(dct)

def process_map(filename):
    st = set()
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="power":
                st.add(element.attrib['v'])
    dct={}
    for item in st:
        dct[item]=0
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="power":
                dct[element.attrib['v']]=dct[element.attrib['v']]+1
    return dct

if __name__ == "__main__":
    test()   
    
    
### 5 audit cuisine
def test():
    dct = process_map('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm')
    pprint.pprint(dct)

def process_map(filename):
    st = set()
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="cuisine":
                if element.attrib['v'].lower() in ('coffe_shop','coffee_shop'):
                    element.attrib['v']='coffee'
                if element.attrib['v'].lower() in ('steak_house','steaks'):
                    element.attrib['v']='steak' 
                if element.attrib['v'].lower() in ('mexican','mexcian_food'):
                    element.attrib['v']='mexican'                     
                st.add(element.attrib['v'].lower())
    dct={}
    for item in st:
        dct[item]=0
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="cuisine":
                if element.attrib['v'].lower() in ('coffe_shop','coffee_shop'):
                    element.attrib['v']='coffee'
                if element.attrib['v'].lower() in ('steak_house','steaks'):
                    element.attrib['v']='steak'   
                if element.attrib['v'].lower() in ('mexican','mexcian_food'):
                    element.attrib['v']='mexican'                 
                dct[element.attrib['v'].lower()]=dct[element.attrib['v'].lower()]+1
    dctFinal={}
    for key in dct:
        if ";" not in key and "," not in key:
            dctFinal[key]=dct[key]
    
    return dctFinal

if __name__ == "__main__":
    test()   
    
    
### 5 audit leisure
def test():
    dct = process_map('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm')
    pprint.pprint(dct)

def process_map(filename):
    st = set()
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="leisure":
                if element.attrib['v']=='Montelucia Resort & Spa':
                    element.attrib['v']='resort'               
                st.add(element.attrib['v'].lower())
    dct={}
    for item in st:
        dct[item]=0
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="leisure":
                if element.attrib['v']=='Montelucia Resort & Spa':
                    element.attrib['v']='resort'             
                dct[element.attrib['v'].lower()]=dct[element.attrib['v'].lower()]+1

    return dct

if __name__ == "__main__":
    test()   
        
### 5 audit power
def test():
    dct = process_map('C:/Users/BenBen/Documents/Google Drive/UD032 mongoDB/Lesson_6/phoenix map.osm')
    pprint.pprint(dct)

def process_map(filename):
    st = set()
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="power":
                if element.attrib['v']=='substation':
                    element.attrib['v']='sub_station'               
                st.add(element.attrib['v'].lower())
    dct={}
    for item in st:
        dct[item]=0
    for _, element in ET.iterparse(filename):
        if element.tag in ("tag"):
            if element.attrib['k']=="power":
                if element.attrib['v']=='substation':
                    element.attrib['v']='sub_station'              
                dct[element.attrib['v'].lower()]=dct[element.attrib['v'].lower()]+1

    return dct

if __name__ == "__main__":
    test()   