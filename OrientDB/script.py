import pyorient
import time
import os


client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect( "root", "011092" )

# creating a db
# db_name = 'GratefulDeadConcerts'
db_name = 'gmt7004'
print 'chegou'

if not client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_create( db_name, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_MEMORY )

client.db_open( db_name, "root", "011092" )



cluster_id = client.command( "insert into SelectedFacilities set dict = " + jsondoc )
client.command(
    "insert into my_class ( 'accommodation', 'work', 'holiday' ) values( 'B&B', 'garage', 'mountain' )"
)

#load file 1
start = time.time()



end = time.time()

print 'Time to upload = '+str(end - start)+' seconds'

client.db_close()