#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# visualise Input article distribution by generating png images.
#
# To run this script, you'll need to install pillow:
#
#   pip install pillow
#

import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#px per bar
barWidth = 8

onePageThickness = 8

xBorder = 16
yBorder = 16


maxPages = 36

imgWidth = xBorder * 2  + 51 * barWidth
imgHeight = yBorder * 2 + onePageThickness * maxPages


font = ImageFont.truetype("Futura.ttc", 21)

articleColours = { 'bp' : '#990D7D', 'gp' : '#FF5D00', 'mc' : '#1B5FD1', 'l' : '#F7280D', 'p' : '#A2CA20', 'a' : '#FFCE00', 'none' : 'lightgrey'}
categoryNames = { 'bp' : "Basic Programming", 'gp' : "Graphics Programming", 'mc' : "Machine Code", 'l' : "Languages", 'p' : "Peripherals", 'a' : "Applications", 'all' : 'All articles', 'none' : 'No highlights'}


def produceChartForCode(articleCode='all'):
	img = Image.new('RGB', (imgWidth, imgHeight), color = 'white')
	draw = ImageDraw.Draw(img, 'RGB')
	
	x = xBorder - barWidth
	y = yBorder

	with open('Input magazine content tagging.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

		next(spamreader)
		next(spamreader)
		next(spamreader)
		
		# idx = 0

		currentIssueNumber = 0
		articlePageOffsetInCurrentIssue = 0

		for row in spamreader:
			print("___ Doing a row, x y = ", x, y, " row = ", row)
			# idx += 1
			# if (idx < 4):
			# 	continue

			articleNumber = row[0]
			issueNumber = row[1]

			print("got issue, article = ", issueNumber, articleNumber)
			# stop at the index article
			if (articleNumber == "270"):
				break

			if (issueNumber != currentIssueNumber):
				x += barWidth
				y = yBorder

				print("=========== new issue! ", issueNumber)
				currentIssueNumber = issueNumber 
				articlePageOffsetInCurrentIssue = 0

			series = row[6]
			pagesInArticle = int(row[5])

			print("series, col =", series, articleColours[series])

			barHeight = pagesInArticle * onePageThickness

			if articleCode != 'all' and series != articleCode:
			# if (series != 'gp'):
				series = 'none'

			print("Drawing bar at ", x, y)
			draw.rectangle([x, y,  x + barWidth - 2, y + barHeight - 2], fill=articleColours[series])

			y += barHeight

	# text for category name
	draw.text((xBorder + 10, imgHeight - 42), "Articles: %s (%s)" % (categoryNames[articleCode], articleCode), fill=(0, 0, 0, 255), font=font)

	img.save('inputChart-%s.png' % articleCode)		


for articleCode in articleColours:
	produceChartForCode(articleCode)

produceChartForCode()

print("DONE -------------------------")


# makePDFFor = "pascal"
# makePDFFor = "escapeadventure"
# makePDFFor = "cliffhanger"
# makePDFFor = "3d"
