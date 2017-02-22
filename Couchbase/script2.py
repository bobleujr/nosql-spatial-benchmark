import time
import os
from couchbase.n1ql import N1QLQuery
from couchbase.bucket import Bucket
from couchbase.exceptions import CouchbaseError


normal_bucket = Bucket('couchbase://localhost/selected-facilities')

try:
	rows = normal_bucket.query('selectedfacilities', 'by_capacity',query=Query.from_any("startkey=200"))
	print rows.length
	query = N1QLQuery("SELECT selectedfacilities.* FROM selectedfacilities WHERE properties.capacity > 200")
	print query.length