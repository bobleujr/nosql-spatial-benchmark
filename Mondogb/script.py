from pymongo import MongoClient
import time
import os
# import matplotlib.pyplot as plt
# import numpy as np

client = MongoClient('localhost', 27017)

# db = client.mydb
db = client.mydb.buildingfootprints

# print db.startup_log

""" 
	Test 1 
	Upload

location = '/Users/paulotabarro/Documents/Nosql/'
command = 'mongoimport --db test --collection rest_test_3 --drop --file selectedfacilities.geojson'
command = 'mongoimport --db test --collection buildingfootprints --drop --file buildingfootprints.geojson'

file1 = 'file1.geojson'
file2 = 'file2.geojson'

start = time.time()

os.system(command)

end = time.time()

print 'Time to upload = '+str(end - start)+' seconds'
"""



""" 
	Test 2
	Query every facility with capacity > 10000


db = client.test.selectedfacilities

start = time.time()

response = list(db.find({"properties.capacity":{ '$gt': 10000 }}))

end = time.time()

print 'Time to select > 10,000 = '+str(end - start)+' seconds'
"""


""" 
	Test 3
	Query all geometries within TopLeft=[-73.995762,40.764826] BottomRight=[-73.934034,40.802038]



db = client.test.selectedfacilities

start = time.time()

response = list(db.find( {
						   'geometry': { '$geoWithin': { '$box':  [ [-73.995762,40.764826], [-73.934034,40.802038] ] } }
						} ))
end = time.time()

print 'Time to select bbox = '+str(end - start)+' seconds'
"""


""" 
	Test 4
	Query all facilities
"""

""" 
	By normal way

"""
db = client.test.selectedfacilities

start = time.time()

response = list(db.find())

end = time.time()

print len(response)
print 'Time to get all selected facilities (normal) = '+str(end - start)+' seconds'

""" 
	By spatial way

"""
db = client.test.selectedfacilities

start = time.time()

response = list(db.find( {
						   'geometry': { '$geoWithin': { '$box':  [ [-180,-180], [180,180] ] } }
						} ))

end = time.time()

print len(response)
print 'Time to get all selected facilities (spatial) = '+str(end - start)+' seconds'


""" 
	Test 5
	Query all building footprints
"""

""" 
	By normal way

"""
db = client.test.buildingfootprints

start = time.time()

response = list(db.find())

end = time.time()

print len(response)
print 'Time to get all building footprints (normal) = '+str(end - start)+' seconds'

""" 
	By spatial way

"""
db = client.test.buildingfootprints

start = time.time()

response = list(db.find( {
						   'geometry': { '$geoWithin': { '$box':  [ [-180,-180], [180,180] ] } }
						} ))

end = time.time()

print len(response)
print 'Time to get all selected facilities (spatial) = '+str(end - start)+' seconds'
