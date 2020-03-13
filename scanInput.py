#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# scanInput.py
#
# THIS PROJECT IS EXTREMELY ROUGH AND READY! But it works (at least for me).
#
# This script scans INPUT magazine metadata and uses qpdf to make pdf extracts
# with articles from various article series.
#
# To run:
#
# Edit the makePDFFor string below to one of the values in comment alongside. (These are all
# values 'series tag' in the speadsheet 'Input magazine content tagging.csv'.)
#
# Then run this script without any arguments:
#
# python scanInput.py 
#

import csv
from subprocess import call


makePDFFor = "3d"
#
# NB:
# all valid values for makePDFFor (and their article counts):
#
# 22 cliffhanger
#  9 adventure
#  6 escapeadventure
#  4 udgs
#  4 3d
#  3 wargame
#  3 typingtutor
#  3 texteditor
#  3 pontoon
#  3 musiccomposer
#  3 foxandgeese
#  3 forth
#  3 flightsim
#  3 commsprites
#  3 calendar
#  2 udggenerator
#  2 spidergame
#  2 secretmessages
#  2 progsinshape
#  2 planningapp
#  2 pascal
#  2 pagedgraphics
#  2 othello
#  2 mininggame
#  2 maze
#  2 logo
#  2 lisp
#  2 intdesign
#  2 hobbiesfiles
#  2 headlines
#  2 hangman
#  2 fruitmachine
#  2 fractals
#  2 commodoreassembler
#  2 commhires
#  2 cad
#  2 assemblingbyhand
#  2 acornsqueezer
#  1 datafile


def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

seriesFound = {}

with open('Input magazine content tagging.csv', 'r') as csvfile:
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
			print("=========== new issue! preamble = ", preamblePageCount)
			currentIssueNumber = issueNumber 
			articlePageOffsetInCurrentIssue = 0

		series = row[8]
		pagesInArticle = row[5]

		print("row=", row)
		print("pages in article =", pagesInArticle)

		if (len(series) > 0):
			print(series)

			if (not series in seriesFound):
				seriesFound[series] = []

			pageNumInIssue = preamblePageCount + articlePageOffsetInCurrentIssue

			# note that first page in an issue is 0.
			seriesArticleRecord = (issueNumber, pageNumInIssue, int(pagesInArticle))
			seriesFound[series].append(seriesArticleRecord)

			# print "seriesFound = ", seriesFound

		articlePageOffsetInCurrentIssue += int(pagesInArticle)

		print("page for article in curr issue = ", articlePageOffsetInCurrentIssue) 

print("DONE -------------------------")

print(seriesFound)


recs = seriesFound[makePDFFor]

cmdStr = ""
	
paramPart = ""

for (issueNum, pageNumInIssue, pagesInArticle) in recs:
	print(issueNum, pageNumInIssue, pagesInArticle)

	pdfFilename = 'inputPDFs/input%s.pdf' % ('%02d' % int(issueNum))
	rangeText = "%s-%s" % (pageNumInIssue + 1, pageNumInIssue + pagesInArticle)

	# paramPart += rangeText
	# print "pdfFilename =", pdfFilename, rangeText

	cmdStr += ' %s %s' % (pdfFilename, rangeText)

print(cmdStr)

fullCmd = "qpdf --empty --pages%s -- %s.pdf" % (cmdStr, makePDFFor)


print("CALLING COMMAND: ", fullCmd.split(' '))
print("CALLING COMMAND: ", fullCmd)

call(fullCmd.split(' '))

	# cmdStr.append()

# qpdf --empty --pages $(for i in *.pdf; do echo $i 1-z; done) -- all.pdf

# for title, deets in seriesFound.items():
# 	print title, len(deets)

