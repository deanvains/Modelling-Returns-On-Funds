from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
from reportlab.lib.validators import Auto
from reportlab.graphics.shapes import Rect, Drawing
from reportlab.lib.colors import Color, blue, red, yellow, green, brown, white, black, HexColor, pink
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Image, SimpleDocTemplate
from flask import make_response
from pathlib import Path
from datetime import date
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.legends import Legend
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

def pdfGen(month,year,fundvalue,interestClass,donation,spending,recapital,distribution,operatingDistribution,additionalContribution,timeframe):
	#Check the inputs
	month = month.strip()
	intMonth = findMonth(month)
	
	if len(year) != 4 or year.isdigit() == False :
		raise Exception("Invalid Years")
	year = int(year)
	value =  fundvalue
	if value.isdigit() == False :
		raise Exception("Invalid Fund Value")
	value = int(fundvalue)
	fprofile = None
	intclass = interestClass.strip()
	interest = InterestRates.query.first()
	
	timeframe = timeframe
	if timeframe.isdigit() == False :
		raise Exception("Invalid Time Frame")
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
	#spending = additionalContribution
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
	if recapital == '' or recapital == '0':
		recap = {}
	else:
		dynVal = recapital.split(',')
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
				recap = calcDyn(recapital,month,year,timeframe)
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
	for t in range(1,timeframe+1,1) :
		temp =  year+t
		horiz.append(str(temp))
	
	#The bits we want on the graph
	opCalc = []
	clCalc = []
	retCalc = []
	donCalc = []
	recCalc = []
	capCalc = []
	for t in range(0,timeframe*12+1,12) :
		opCalc.append(calc[0][t])
		clCalc.append(calc[1][t])
		if not calc[2]:
			retCalc.append(0)
		else:
			retCalc.append(calc[2][t])
		if not calc[3]:
			donCalc.append(0)
		else:
			donCalc.append(calc[3][t])
		if not calc[4]:
			recCalc.append(0)
		else:
			recCalc.append(calc[4][t])
		if not calc[5]:
			capCalc.append(0)
		else:
			capCalc.append(calc[5][t])


	data = []
	data2 = []
	tuple(opCalc)
	tuple(clCalc)
	tuple(retCalc)
	tuple(donCalc)
	tuple(recCalc)
	tuple(capCalc)
	data.append(opCalc)
	data.append(clCalc)
	#data.append(retCalc)
	data2.append(donCalc)
	data2.append(recCalc)
	data2.append(capCalc)
	tuple(data)
	tuple(data2)
	#Create the PDF file
	import io
	output = io.BytesIO()

	c = canvas.Canvas(output)
	
	
	c.setFillColor(HexColor("#27348b")) #UWA Blue
	c.rect(0, 765, 600, 80, stroke =0, fill = 1)
	c.setFillColor(HexColor("#e2b600")) #UWA Yellow
	c.rect(0, 755, 600, 10, stroke=0, fill=1)
	c.rect(0, 0, 600, 15, stroke=0, fill=1)
	#Put in the footer information
	c.setFillColor(HexColor("#464646"))
	c.setFont("Helvetica", 9)
	today = date.today()
	c.drawString(10,17,str(today))
	c.drawString(200,17,"Treasury, Investments & Financial Compliance")
	c.drawString(450,17,"")
	#Put in a informative paragraph
	textobject = c.beginText()
	textobject.setTextOrigin(inch, 10*inch)
	#Page title
	textobject.setFillColor(HexColor("#27348b"))
	textobject.setFont("Helvetica-Bold",20)
	textobject.textLine(text = 'Modelling Returns on Funds')
	#Intro sentence
	textobject.setFont("Helvetica", 10)
	textobject.setFillColor(black)
	text = 'Thank you for using the Modelling Returns on Funds Online Tool. This tool was developed in order to '
	textobject.textLine(text = text)
	text = 'estimate the returns generated by funds managed by the Treasury, Investments & Financial Compliance '
	textobject.textLine(text = text)
	text = 'Office of UWA. The results were generated automatically based on the variables inputted below. With an '
	textobject.textLine(text = text)
	text = 'account, previous results can be accessed from Stored results portal of the Online Tool.'
	textobject.textLine(text = text)
	textobject.textLine()
	#Set the header setting and fill in
	textobject.setFillColor(HexColor("#313764"))
	textobject.setFont("Helvetica-Bold",15)
	textobject.textLine(text = 'Inputs Used')
	#Set the actual content setting and write in
	textobject.setFont("Helvetica", 10)
	textobject.setFillColor(black)
	textobject.textLine(text = 'Starting Date: ' + month.capitalize() + ' ' + str(year))
	textobject.textLine(text = 'Interest Class: '+intclass)

	textobject.textLine(text = 'Initial Fund Value: $' + str(value))
	textobject.textLine(text = 'Fund Time Length: ' + str(timeframe) + ' Years')

	textobject.textLine(text = 'Distribution Rate: ' + str(distribution*100) + '%')

	c.drawText(textobject)

	path = str(Path(__file__).parent)
	
	logo = Image.open(path+"/static/UWA-Logo.png")
	width, height = logo.size
	c.drawImage(path+"/static/UWA-Logo.png",10,780,width/2,height/2,mask='auto')

	maxY = 0
	for i in range(len(calc[0])):
		if calc[0][i] > maxY :
			maxY = calc[0][i]

	maxY2 = 50 * ceil(maxY/50)
	
	drawing = Drawing(400,150)
	lc = HorizontalLineChart()
	lc.x = 50
	lc.y = 50
	lc.height = 200
	lc.width = 300
	lc.data = data
	lc.joinedLines = 1
	lc.categoryAxis.categoryNames = horiz
	lc.categoryAxis.labels.boxAnchor = 'n'
	lc.valueAxis.valueMin = 0
	lc.valueAxis.valueMax = maxY2
	lc.valueAxis.valueStep = round(maxY2/10)
	lc.lines[0].strokeWidth = 1
	lc.lines[1].strokeWidth = 1

	#lc.lines[2].strokeWidth = 0


	#lc.lines[4].strokeWidth = 1

	#lc.lines[5].strokeWidth = 1
	
	lc.lineLabelFormat = '%2.0f'
	for o in range(0,len(data[1])):
		lc.lineLabels[(1,o)].dy = -20
		#lc.lineLabels[(2,o)].visible = False
		
	
	drawing.add(lc)

	#drawing.drawOn(c,100,300)
	legend = Legend()
	legend.alignment = 'right'
	legend.x = 10
	legend.y = 10
	legend.colorNamePairs = ((red,'Opening Balance'),(green,'Closing Balance'))#,(blue,'Interest Returns'))
	
	drawing.add(legend)

	drawing.drawOn(c,100,250)

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
