import re

with open('/home/vagrant/patentdata/patent-1.txt'):
	for line in f:
		match = regex.search(line)
		print match.group(1)
