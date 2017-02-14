import pyorient
import time
import os


client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect( "admin", "admin" )

# creating a db
db_name = 'gmt7004'
if not client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_create( db_name, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )

client.db_open( db_name, "root", "011092" )

#load file 1
start = time.time()

end = time.time()

print 'Time to upload = '+str(end - start)+' seconds'

