import json
import sys

filename = sys.argv[1]
data = json.load(open(str(filename)))
for i in xrange(0, len(data)):
   # treeid = data[i]['TREE_ID']
   outfile = open('./output/' + str(i) + '.geojson', 'w+')
   # print data
   json.dump(data[i], outfile)
   outfile.close()