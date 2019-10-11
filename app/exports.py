from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.graphics.shapes import Rect, Drawing
from reportlab.lib.colors import Color, blue, red, yellow, green, brown, white, black, HexColor
from flask import make_response
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from PIL import Image

from calculations.ClassH import classH
from calculations.ClassN import classN
from calculations.ClassQ import classQ
from calculations.ClassE import classE
from calculations.ClassA import classA
from calculations.ClassF import classF
from calculations.ClassG import classG
from calculations.ClassS import classS
from calculations.findDec import findDec
from calculations.calDynamic import calcDyn
from calculations.calcMonth import calcMonths
from app.models import User, InterestRates, expected

def pdfGen(month,year,fundvalue,interestClass,donation,spending,recap,distribution,operatingDistribution,additionalContribution,timeframe):
	#Check the inputs
	month = month.strip()
	fprofile = None
	interest = InterestRates.query.first()
	intclass = interestClass.strip()
	
	if donation == '' or donation == '0':
		donation = {}
	else:
		dynVal = donation.split(',')
		yearValue = 0
		for group in dynVal:
			grpLst = group.split("-")
			if len(grpLst) == 3 :
				monthVal = grpLst[0].strip().lower()
				yearVal = grpLst[1].strip()
				if yearVal.isdigit() == True :
					if int(yearVal) < int(yearValue) :
						raise Exception("Year 2 is lower than year 1")
					else:
						yearValue = yearVal
		donation = calcDyn(donation,month,year,timeframe)

	if spending == '' or spending == '0' :
		spending = {}
	else:
		dynVal = spending.split(',')
		yearValue = 0
		for group in dynVal:
			grpLst = group.split("-")
			if len(grpLst) == 3 :
				monthVal = grpLst[0].strip().lower()
				yearVal = grpLst[1].strip()
				if yearVal.isdigit() == True :
					if int(yearVal) < int(yearValue) :
						raise Exception("Year 2 is lower than year 1")
					else:
						yearValue = yearVal
		spending = calcDyn(spending,month,year,timeframe)

	if recap == '' or recap == '0':
		recap = {}
	else:
		dynVal = recap.split(',')
		yearValue = 0
		for group in dynVal:
			grpLst = group.split("-")
			if len(grpLst) == 3 :
				monthVal = grpLst[0].strip().lower()
				yearVal = grpLst[1].strip()
				if yearVal.isdigit() == True :
					if int(yearVal) < int(yearValue) :
						raise Exception("Year 2 is lower than year 1")
					else:
						yearValue = yearVal
		recap = calcDyn(recap,month,year,timeframe)

	if operatingDistribution == '' or operatingDistribution == '0' :
		operatingDistribution = {}
	else:
		dynVal = operatingDistribution.split(',')
		yearValue = 0
		for group in dynVal:
			grpLst = group.split("-")
			if len(grpLst) == 3 :
				monthVal = grpLst[0].strip().lower()
				yearVal = grpLst[1].strip()
				
				if yearVal.isdigit() == True :
					if int(yearVal) < int(yearValue) :
						raise Exception("Year 2 is lower than year 1")
					else:
						yearValue = yearVal
		operatingDistribution = calcDyn(operatingDistribution,month,year,timeframe)

	if additionalContribution == '' or additionalContribution == '0':
		addContribution = {}
	else:
		dynVal = additionalContribution.split(',')
		yearValue = 0
		for group in dynVal:
			grpLst = group.split("-")
			if len(grpLst) == 3 :
				monthVal = grpLst[0].strip().lower()
				yearVal = grpLst[1].strip()
				if yearVal.isdigit() == True :
					if int(yearVal) < int(yearValue) :
						raise Exception("Year 2 is lower than year 1")
					else:
						yearValue = yearVal
		addContribution = calcDyn(additionalContribution,month,year,timeframe)
	decMonth = findDec(month)

	#Perform the correct calculation
	if intclass == "E":
		thisinterest = interest.ClassE
		calc = classE(month,year,fundvalue,fprofile,intclass,thisinterest,donation,recap,distribution,timeframe)
	elif intclass == "F":
		thisinterest = interest.ClassF
		calc = classF(month,year,fundvalue,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
	elif intclass == "G" :
		thisinterest = interest.ClassG
		calc = classG(month,year,fundvalue,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
	elif(intclass == "H"):
		thisinterest = interest.ClassH
		calc = classH(month,year,fundvalue,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
	elif intclass == "A":
		thisinterest = interest.ClassA
		calc = classA(month,year,fundvalue,fprofile,intclass,thisinterest,spending,recap,operatingDistribution,timeframe)
	elif(intclass == "N"):
		thisinterest = interest.ClassN
		calc = classN(month,year,fundvalue,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
	elif(intclass == "Q"):
		thisinterest = interest.ClassQ
		calc = classQ(month,year,fundvalue,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
	elif(intclass == "S"):
		thisinterest = interest.ClassS
		calc = classS(month,year,fundvalue,fprofile,intclass,thisinterest,spending,addContribution,timeframe)

	#This is getting disgustingly long, bad coding mate
	monthlist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	horiz = []
	horiz[0] = monthlist[11 - decMonth]
	for k in range(len(calc[1])) :
		if k == len(calc[1])/12 :
			horiz.append(monthlist[k%12-1])
		else :
			horiz.append('')
	


	#Create the PDF file
	import io
	output = io.BytesIO()

	c = canvas.Canvas(output)

	c.drawString(100,100,"Hello World")
	c.setFillColor(HexColor("#332FA7"))
	c.rect(0, 765, 600, 80, stroke =0, fill = 1)
	c.setFillColor(HexColor("#FCD433"))
	c.rect(0, 755, 600, 10, stroke=0, fill=1)
	#Put in a informative paragraph
	c.setFillColor(black)
	textobject = c.beginText()
	textobject.setTextOrigin(inch, 10*inch)
	textobject.setFont("Helvetica", 10)
	textobject.textLine(text = month)
	textobject.textLine(text = intclass)
	textobject.textLine(text = '    Make everything dynamic')
	textobject.textLine(text = '    Better Graph')
	textobject.textLine(text = '    UWA logo')
	textobject.textLine(text = '    Connect to website and check how to download')
	textobject.setFillGray(0.4)
	c.drawText(textobject)


	#logo = Image.open("/static/UWA-Logo.png")

	#c.drawImage("UWA-Logo.png",100,100)



	maxY = 0
	for i in range(len(calc[1])):
		if calc[1][i] > maxY :
			maxY = calc[1][i]

	drawing = Drawing(400,200)
	lc = HorizontalLineChart()
	lc.x = 50
	lc.y = 50
	lc.height = 300
	lc.width = 500
	lc.data = calc
	lc.joinedLines = 1
	catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
	lc.categoryAxis.categoryNames = catNames
	lc.categoryAxis.labels.boxAnchor = 'n'
	lc.valueAxis.valueMin = 0
	lc.valueAxis.valueMax = maxY
	lc.valueAxis.valueStep = round(maxY/6)
	lc.lines[0].strokeWidth = 2
	lc.lines[1].strokeWidth = 1.5
	drawing.add(lc)

	drawing.drawOn(c,100,300)

	c.showPage()
	c.save()

	pdf_out = output.getvalue()
	output.close()

	response = make_response(pdf_out)
	response.headers['Content-Disposition'] = "attachment; filename=model.pdf"
	response.mimetype = 'application/pdf'
	return response
