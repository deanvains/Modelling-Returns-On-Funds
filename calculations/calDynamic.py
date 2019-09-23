from calculations.calcMonth import calcMonths


def calcDyn(dynamicVal,startMonth,startYear,dur):
    monthDict = {"jan" : 1,
                 "feb" : 2,
                 "mar" : 3,
                 "apr" : 4,
                 "may" : 5,
                 "jun" : 6,
                 "jul" : 7,
                 "aug" : 8,
                 "sep" : 9,
                 "oct" : 10,
                 "nov" : 11,
                 "dec" : 12}

    calc = {}
    for i in range(dur*12+1):
        calc[i] = 0
    
    dynVal = dynamicVal.split(" ")
    for group in dynVal:
        grpLst = group.split("-")
        print(grpLst)
        monthVal = grpLst[0].lower()
        yearVal = grpLst[1]
        moneyVal = int(grpLst[2])
        startVal = calcMonths(startYear,int(yearVal),monthDict[startMonth.lower()],monthDict[monthVal])
        print(startVal)
        for i in range(startVal,dur*12+1):
            calc[i] = moneyVal
    print(dynamicVal)        
    print(calc)        
    return calc  
    