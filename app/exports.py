from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import Color, blue, red, yellow, green, brown, white, black, HexColor
from flask import make_response
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart

def pdfGen():
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
    textobject.textLine(text = 'This is an automatically generated pdf.')
    textobject.textLine(text = 'To do:')
    textobject.textLine(text = '    Make everything dynamic')
    textobject.textLine(text = '    Better Graph')
    textobject.textLine(text = '    UWA logo')
    textobject.textLine(text = '    Connect to website and check how to download')
    textobject.setFillGray(0.4)
    c.drawText(textobject)
    
    
    drawing = Drawing(400,200)
    data = [
            (13, 5, 20, 22, 37, 45, 19, 4),
            (5, 20, 46, 38, 23, 21, 6, 14)
            ]
    lc = HorizontalLineChart()
    lc.x = 50
    lc.y = 50
    lc.height = 125
    lc.width = 300
    lc.data = data
    lc.joinedLines = 1
    catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
    lc.categoryAxis.categoryNames = catNames
    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.valueAxis.valueMin = 0
    lc.valueAxis.valueMax = 60
    lc.valueAxis.valueStep = 15
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
    print(response)
    return response
