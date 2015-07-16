'''
patent,Cit_Date,Cit_Name,Cit_Kind,Cit_Country,Citation,Category,CitSeq
06009555,1980-03-01,FAY,"",,04192017,,
06009555,1985-10-01,"BROWN ET AL.","",,04547903,,
'''

import csv
import re

with open("patent.csv","rb") as source:
    rdr= csv.reader(source)
    with open("patent-processed.csv","wb") as result:
        wtr= csv.writer(result, delimiter=",")
        for r in rdr:
            wtr.writerow((re.sub(r'\D', '', str(r[0])), r[6], r[8]))

