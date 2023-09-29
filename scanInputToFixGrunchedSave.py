#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Fix the CSV for my knackered spreadsheet (yeah, I saved it as CSV, and it split all titles, ffs, idioten!)
#
#

import csv

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

outFile = open('result.csv', 'w')

spamwriter = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


with open('Input magazine content tagging.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		idx = 1
		while (not (representsInt(row[idx])) or row[idx] == "-"):
			print "skipping ", row[idx]
			idx += 1

		print "final: ", row[idx]
		# special case - jump over the split-out number following the '-'
		if (row[idx - 1] == "-"):
			print "********* got the special case!"
			idx += 1

		print "*** we stopped at ", row[idx]

		title = [ ' '.join(row[1:idx]) ]
		restOfData = row[idx:idx + 6]

		print title[0]
		print title[0][-1]

		if (title[0][-1] == '-'):
			print "found a weird one for ", title
		# print "parts: ", title, " and ", restOfData
		title.extend(restOfData)

		# print title
		
		spamwriter.writerow(title)
		# print "title=", title, "rest of data=", restOfData

		# print ' '.join(row[1:idx + 4])


outFile.close()

list1 = [2,3]
list2 = [4,5]
list1.extend(list2)
print list1
