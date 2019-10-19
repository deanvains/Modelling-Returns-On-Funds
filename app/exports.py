from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
from reportlab.graphics.shapes import Rect, Drawing
from reportlab.lib.colors import Color, blue, red, yellow, green, brown, white, black, HexColor
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Image, SimpleDocTemplate
from flask import make_response
from pathlib import Path
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.legends import LineLegend
from PIL import Image
from math import ceil
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
from calculations.findMonth import findMonth
from app.models import User, InterestRates, expected

def pdfGen(month,year,value,interestClass,donation,spending,recap,distribution,operatingDistribution,additionalContribution,timeframe):
	#Check the inputs
	month = month.strip()
	intMonth = findMonth(month)
	if len(year) != 4 or year.isdigit() == False :
		raise Exception("Invalid Years")
	year = int(year)
	value = int(value)
	fprofile = None
	intclass = interestClass.strip()
	interest = InterestRates.query.first()
	timeframe = int(timeframe)
	
	if donation == '' or donation == '0':
		donation = {}
	else:
		dynVal = donation.split(',')
		yearValue = 0
		for group in dynVal:
			grpLst = group.split("-")
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
		calc = classE(month,year,value,fprofile,intclass,thisinterest,donation,recap,distribution,timeframe)
	elif intclass == "F":
		thisinterest = interest.ClassF
		calc = classF(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
	elif intclass == "G" :
		thisinterest = interest.ClassG
		calc = classG(month,year,value,fprofile,intclass,thisinterest,donation,recap,operatingDistribution,timeframe)
	elif(intclass == "H"):
		thisinterest = interest.ClassH
		calc = classH(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
	elif intclass == "A":
		thisinterest = interest.ClassA
		calc = classA(month,year,value,fprofile,intclass,thisinterest,spending,recap,operatingDistribution,timeframe)
	elif(intclass == "N"):
		thisinterest = interest.ClassN
		calc = classN(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
	elif(intclass == "Q"):
		thisinterest = interest.ClassQ
		calc = classQ(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
	elif(intclass == "S"):
		thisinterest = interest.ClassS
		calc = classS(month,year,value,fprofile,intclass,thisinterest,spending,addContribution,timeframe)
	
	#This is getting disgustingly long, bad coding mate
	#Create the horizontal list of years
	horiz = [str(year)]
	for t in range(1,timeframe,1) :
		temp =  year+t
		horiz.append(str(temp))
	
	#The bits we want on the graph, should probably make a table as well
	opCalc = []
	clCalc = []
	for t in range(0,timeframe*12,12) :
		opCalc.append(calc[0][intMonth+t])
		clCalc.append(calc[1][intMonth+t])
	data = []
	tuple(opCalc)
	tuple(clCalc)
	data.append(opCalc)
	data.append(clCalc)
	tuple(data)

	#Create the PDF file
	import io
	output = io.BytesIO()

	c = canvas.Canvas(output)
	
	
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

	path = str(Path(__file__).parent)
	
	logo = Image.open(path+"/static/UWA-Logo.png")

	c.drawImage(path+"/static/UWA-Logo.png",100,100,100,100,)

	maxY = 0
	for i in range(len(calc[0])):
		if calc[1][i] > maxY :
			maxY = calc[0][i]

	maxY2 = 50 * ceil(maxY/50)
	
	drawing = Drawing(400,200)
	lc = HorizontalLineChart()
	lc.x = 50
	lc.y = 50
	lc.height = 125
	lc.width = 300
	lc.data = data
	lc.joinedLines = 1
	lc.categoryAxis.categoryNames = horiz
	lc.categoryAxis.labels.boxAnchor = 'n'
	lc.valueAxis.valueMin = 0
	lc.valueAxis.valueMax = maxY2
	lc.valueAxis.valueStep = round(maxY2/10)
	lc.lines[0].strokeWidth = 2
	lc.lines[1].strokeWidth = 1.5

	
	drawing.add(lc)

	drawing.drawOn(c,100,300)

	#Lets make a table, what could possible go wrong!
	temp = [str(data[0][0])]
	
	for g in range(1,len(data[0])):
		temp.append(str(data[0][g]))
	
	#horiz.append(list(data[0]))
	#horiz.append(list(data[1]))
	tble = Table(temp,colWidths=10*mm)
	tble.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),("ALIGN", (0,0), (-1,-1), "CENTER"),('INNERGRID', (0,0), (-1,-1), 0.25, black)])
	#tble.wrapOn(c, A4, A4)
	#tble.drawOn(c,100,100)

	c.showPage()
	c.save()

	pdf_out = output.getvalue()
	output.close()

	response = make_response(pdf_out)
	response.headers['Content-Disposition'] = "attachment; filename=model.pdf"
	response.mimetype = 'application/pdf'
	return response
