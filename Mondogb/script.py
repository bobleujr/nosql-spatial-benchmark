from pymongo import MongoClient
import time
import os
# import matplotlib.pyplot as plt
# import numpy as np

client = MongoClient('localhost', 27017)

# db = client.mydb
db = client.mydb.rest_test_4

# print db.startup_log

#
# location = '/Users/paulotabarro/Documents/Nosql/'
# command = 'mongoimport --db test --collection rest_test_3 --drop --file selectedfacilities.geojson'
command = 'mongoimport --db test --collection rest_test_4 --drop --file buildingfootprints.geojson'
# file1 = 'file1.geojson'
# file2 = 'file2.geojson'


#load file 1
start = time.time()

os.system(command)

end = time.time()

print 'Time to upload = '+str(end - start)+' seconds'


#1
start = time.time()

db.count()

end = time.time()


print 'Time to count = '+str(end - start)+' seconds'

#2
start = time.time()

db.find({"borough":"Brooklyn"})

end = time.time()


print 'Time to find Brooklyn = '+str(end - start)+' seconds'

