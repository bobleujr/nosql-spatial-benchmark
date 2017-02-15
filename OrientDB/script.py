import pyorient
import time
import os


client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect( "root", "011092" )

# creating a db
db_name = 'gmt7004'

if not client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_create( db_name, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )

client.db_open( db_name, "root", "011092" )

#load file 1
start = time.time()

with open('selectedfacilities.json') as data_file:
	for jsondoc in data_file:
		client.command( "insert into SelectedFacilities set dict = " + jsondoc )


end = time.time()

print 'Time to upload = '+str(end - start)+' seconds'

client.db_close()