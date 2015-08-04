import re

f = open('/home/vagrant/patentdata/patent-1.txt', 'r'):
	
for line in f:	
	if re.match("^\d+\ \d+$", line):
		print line
