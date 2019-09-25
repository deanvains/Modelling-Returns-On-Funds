from calculations.ClassS import classS

def testdata():
    month = 'jan'
    year = 2019
    fundValue = 800000
    fProfile = None
    interestClass = 'N'
    interest = 0.015
    #i and spendAmount will not included in parameters, I used it here to populate the dictionary required for spending,
    #in our project, form should have a variable that stores a dictionary that can be passed here
    i = 0
    spendAmount = 16000
    
    spending = {}
    while i != 48:
        spending[i] = spendAmount
        i += 1
        if i == 12:
            spendAmount = 17000
        if i == 24:
            spendAmount = 17000
        if i == 36:
            spendAmount = 18000
    addContri = {}
    for i in range(48):
        addContri[i] = None
        
    timeframe = 48
    result = classS(month,year,fundValue,fProfile,interestClass,interest,spending,addContri,timeframe)
    return result