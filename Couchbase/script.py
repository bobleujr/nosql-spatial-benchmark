import time
import os
from couchbase.n1ql import N1QLQuery


from couchbase.bucket import Bucket
from couchbase.exceptions import CouchbaseError

# c = Bucket('couchbase://localhost/gmt7004')

# try:
#     beer = c.get("aass_brewery-juleol")

# except CouchbaseError as e:
#     print "Couldn't retrieve value for key", e
#     # Rethrow the exception, making the application exit
#     raise

# doc = beer.value

# # Because Python 2.x will complain if an ASCII format string is used
# # with Unicode format values, we make the format string unicode as well.


# print unicode("{name}, ABV: {abv}").format(name=doc['name'], abv=doc['abv'])

# doc['comment'] = "Random beer from Norway"

# try:
#     result = c.replace("aass_brewery-juleol", doc)
#     print result

# except CouchbaseError as e:
#     print "Couldn't replace key"
#     raise



command = "'/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbdocloader' -u admin -p 011092 -n 127.0.0.1 -b building-footprint output.zip"

# load file 1
start = time.time()

os.system(command)

end = time.time()

print 'Time to upload = '+str(end - start)+' seconds'


# #1
# start = time.time()

# db.count()

# end = time.time()


# print 'Time to count = '+str(end - start)+' seconds'

# #2
# start = time.time()

# db.find({"borough":"Brooklyn"})

# end = time.time()


# print 'Time to find Brooklyn = '+str(end - start)+' seconds'

