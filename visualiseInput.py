#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# visualise Input articles
#
#
import csv
from PIL import Image

with open('Input magazine content tagging - recover.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

	idx = 0

	currentIssueNumber = 0
	articlePageOffsetInCurrentIssue = 0

	for row in spamreader:
		idx += 1
		if (idx < 4):
			continue

		articleNumber = row[0]
		issueNumber = row[1]

		# stop at the index article
		if (articleNumber == "270"):
			break

		if (issueNumber != currentIssueNumber):
			print "=========== new issue! ", issueNumber
			currentIssueNumber = issueNumber 
			articlePageOffsetInCurrentIssue = 0

		series = row[6]
		pagesInArticle = row[3]


print "DONE -------------------------"


# makePDFFor = "pascal"
# makePDFFor = "escapeadventure"
# makePDFFor = "cliffhanger"
# makePDFFor = "3d"
