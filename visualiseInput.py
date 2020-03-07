#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# visualise Input articles
#
#
import csv
from PIL import Image
from PIL import ImageDraw

#px per bar
barWidth = 8

onePageThickness = 8

xBorder = 16
yBorder = 16

x = xBorder
y = yBorder

maxPages = 50

img = Image.new('RGB', (xBorder * 2  + 51 * (barWidth + 1), yBorder * 2 + onePageThickness * maxPages), color = 'white')
draw = ImageDraw.Draw(img, 'RGB')

articleColours = { 'bp' : 'red', 'gp' : 'green', 'mc' : 'blue', 'l' : 'purple', 'p' : 'grey', 'a' : 'cyan', 'none' : 'lightgrey'}

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
			x += barWidth
			y = yBorder

			print "=========== new issue! ", issueNumber
			currentIssueNumber = issueNumber 
			articlePageOffsetInCurrentIssue = 0

		series = row[6]
		pagesInArticle = int(row[5])

		print "series, col =", series, articleColours[series]

		barHeight = pagesInArticle * onePageThickness

		if (series != 'l'):
		# if (series != 'gp'):
			series = 'none'

		draw.rectangle([x, y,  x + barWidth - 2, y + barHeight - 2], fill=articleColours[series])

		y += barHeight

img.save('inputChart.png')		

print "DONE -------------------------"


# makePDFFor = "pascal"
# makePDFFor = "escapeadventure"
# makePDFFor = "cliffhanger"
# makePDFFor = "3d"
