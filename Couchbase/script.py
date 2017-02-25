import time
import os
import requests
from couchbase.n1ql import N1QLQuery
from couchbase.bucket import Bucket
from couchbase.exceptions import CouchbaseError
from couchbase.views.params import Query
from couchbase.views.iterator import View



""" 
TEST 1

command = "'/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbdocloader' -u admin -p 011092 -n 127.0.0.1 -b building-footprint output.zip"

# load file 1
start = time.time()

os.system(command)

end = time.time()

print 'Time to upload = '+str(end - start)+' seconds'

"""


""" 
	Test 2
	Query every facility with capacity > 10000
"""
"""
"""
url_base = "http://127.0.0.1:8092/selected-facilities"
design = "/_design/dev_by_capacity"
view = "/_view/by_capacity"
params = "?startkey=10000"
final_params = "&full_set=true"


start = time.time()

response = requests.get(url_base+design+view+params+final_params)

end = time.time()

print len(response.json()['rows'])
# print response.json()
print 'Time to query = '+str(end - start)+' seconds'





""" 
	Test 3
	Query all geometries within TopLeft=[-73.995762,40.764826] BottomRight=[-73.934034,40.802038]
"""
url_base = "http://127.0.0.1:8092/selected-facilities"
design = "/_design/dev_facilities"
view = "/_spatial/facilities"
params = "?start_range=[-73.995762,40.764826]&end_range=[-73.934034,40.802038]"
final_params = "&full_set=true"

start = time.time()

response = requests.get(url_base+design+view+params+final_params)

end = time.time()

# print response.json()
print len(response.json()['rows'])
print 'Time to query = '+str(end - start)+' seconds'




""" 
	Test 4
	Query all facilities by normal vs spatial view
"""
"""
"""
url_base = "http://127.0.0.1:8092/selected-facilities"
design = "/_design/dev_by_capacity"
view = "/_view/by_capacity"
params = "?"
final_params = "&full_set=true"


start = time.time()

response = requests.get(url_base+design+view+params+final_params)

end = time.time()

print len(response.json()['rows'])
print 'Time to query = '+str(end - start)+' seconds'

design = "/_design/dev_facilities"
view = "/_spatial/facilities"
params = "?start_range=[-90,-90]&end_range=[90,90]"
final_params = "&full_set=true"

start = time.time()

response = requests.get(url_base+design+view+params+final_params)

end = time.time()

# print response.json()
print len(response.json()['rows'])
print 'Time to query = '+str(end - start)+' seconds'




""" 
	Test 5
	Query all facilities by normal vs spatial view
"""

url_base = "http://127.0.0.1:8092/building-footprint"
design = "/_design/dev_bin"
view = "/_view/by_bin"
params = "?"
final_params = "full_set=true"


start = time.time()

response = requests.get(url_base+design+view+params+final_params)

end = time.time()

print len(response.json()['rows'])
print 'TTime to query building footprints normally = '+str(end - start)+' seconds'

design = "/_design/dev_all"
view = "/_spatial/by_geometry"
params = "?start_range=[-90,-90]&end_range=[90,90]"
final_params = "&full_set=true"

start = time.time()

response = requests.get(url_base+design+view+params+final_params)

end = time.time()

# print response.json()
print len(response.json()['rows'])
print 'Time to query building footprints spatially = '+str(end - start)+' seconds'


