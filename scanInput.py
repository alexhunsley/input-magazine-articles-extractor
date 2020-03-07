#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Scan input metadata and make pdf extracts with articles from various
#
#

import csv
from subprocess import call

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

seriesFound = {}

with open('Input magazine content tagging - recover.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')


	idx = 0

	currentIssueNumber = 0
	articlePageOffsetInCurrentIssue = 0

	for row in spamreader:
		idx += 1
		if (idx < 4):
			continue

		preamblePageCount = 2
		if (idx == 4):
			# first issue of input has three preamble pages (the green keyboard page is in there)
			preamblePageCount = 3

		articleNumber = row[0]
		issueNumber = row[1]

		# stop at the index article
		if (articleNumber == "270"):
			break

		if (issueNumber != currentIssueNumber):
			print "=========== new issue! preamble = ", preamblePageCount
			currentIssueNumber = issueNumber 
			articlePageOffsetInCurrentIssue = 0

		series = row[8]
		pagesInArticle = row[5]

		print "row=",row
		print "pages in article =", pagesInArticle

		if (len(series) > 0):
			print series

			if (not series in seriesFound):
				seriesFound[series] = []

			pageNumInIssue = preamblePageCount + articlePageOffsetInCurrentIssue

			# note that first page in an issue is 0.
			seriesArticleRecord = (issueNumber, pageNumInIssue, int(pagesInArticle))
			seriesFound[series].append(seriesArticleRecord)

			# print "seriesFound = ", seriesFound

		articlePageOffsetInCurrentIssue += int(pagesInArticle)

		print "page for article in curr issue = ", articlePageOffsetInCurrentIssue 

print "DONE -------------------------"

print seriesFound

# makePDFFor = "pascal"
# makePDFFor = "escapeadventure"
# makePDFFor = "cliffhanger"
# makePDFFor = "3d"
makePDFFor = "adventure"

recs = seriesFound[makePDFFor]

cmdStr = ""
	
paramPart = ""

for (issueNum, pageNumInIssue, pagesInArticle) in recs:
	print issueNum, pageNumInIssue, pagesInArticle

	pdfFilename = 'allInOneFolder/input%s.pdf' % ('%02d' % int(issueNum))
	rangeText = "%s-%s" % (pageNumInIssue + 1, pageNumInIssue + pagesInArticle)

	# paramPart += rangeText
	# print "pdfFilename =", pdfFilename, rangeText

	cmdStr += ' %s %s' % (pdfFilename, rangeText)

print cmdStr

fullCmd = "qpdf --empty --pages%s -- %s.pdf" % (cmdStr, makePDFFor)


print "CALLING COMMAND: ", fullCmd.split(' ')
print "CALLING COMMAND: ", fullCmd

call(fullCmd.split(' '))

	# cmdStr.append()

# qpdf --empty --pages $(for i in *.pdf; do echo $i 1-z; done) -- all.pdf

# for title, deets in seriesFound.items():
# 	print title, len(deets)

