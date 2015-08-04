import re

f = open("citation-processed.csv", "r")
o = open("citation.txt", "w")
for line in f:
        if re.match("^\d+ \d+$", line.rstrip('\r\n')):
                print >> o, line,
