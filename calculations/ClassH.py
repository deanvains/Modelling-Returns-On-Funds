def classH(month,year,value,fprofile,intclass,interest,spending,addContribution,timeframe):
    monthDict = {"January" : 1,
                 "February" : 2,
                 "March" : 3,
                 "April" : 4,
                 "May" : 5,
                 "June" : 6,
                 "July" : 7,
                 "August" : 8,
                 "September" : 9,
                 "October" : 10,
                 "November" : 11,
                 "December" : 12}
    
    
    dateMonth = month
    dateYear = year
    timeFrame = timeframe
    fundValue = value
    fundProfile = fprofile
    interestClass = intclass
    interest = interest
    spendingProfile = spending
    if type(addContribution) == str:
        addContribution = {}
    additionalCapital = addContribution
    
        
        
    monthlyOpBalance = {}
    monthlyClBalance = {}
    monthlyReturn = {}
    annualAMB = {}
            
       
    for month in range(0,timeFrame * 12 + 1):
        if month == 0 and dateMonth == "December":
            monthlyOpBalance[month] = fundValue
            monthlyClBalance[month] = monthlyOpBalance[month]
            if spendingProfile.get(month) != None:
                 monthlyClBalance[month] = int(monthlyClBalance[month] - spendingProfile.get(month))
            if additionalCapital.get(month) != None:
                monthlyClBalance[month] += int(additionalCapital.get(month))
            annualAMB[1] = int(monthlyOpBalance[month])   

        elif month == 0 and dateMonth != "December" :
            monthlyOpBalance[month] = fundValue
            monthlyClBalance[month] = int(monthlyOpBalance[month])
            if spendingProfile.get(month) != None:
                 monthlyClBalance[month] = int(monthlyClBalance[month] - spendingProfile.get(month))
            if additionalCapital.get(month) != None:
                monthlyClBalance[month] += int(additionalCapital.get(month))
        
        elif month > 0 and ((monthDict[dateMonth] + month ) % 12) == 0:
            monthlyOpBalance[month] = monthlyClBalance[month-1]
            sum = 0
            sumAWB = 0
            if month < 12:
                for bal in range(month+1,0,-1):
                    sum += monthlyOpBalance[month - bal + 1]
                annualAMB[(monthDict[dateMonth] + month)/12] = int(sum / (month+1))
                
            else :
                for bal in range(12,12-12,-1):
                    sum += monthlyOpBalance[month - bal+1]
                annualAMB[(monthDict[dateMonth] + month)/12] = int(sum / 12)
            
            monthlyReturn[month] =  int(annualAMB[(monthDict[dateMonth] + month)/12] * float(interest))
            monthlyClBalance[month] =  monthlyOpBalance[month] + monthlyReturn[month] 
            if spendingProfile.get(month) != None:
                 monthlyClBalance[month] = int(monthlyClBalance[month] - spendingProfile.get(month))
            if additionalCapital.get(month) != None:
                monthlyClBalance[month] += int(additionalCapital.get(month))

          
        else :
            monthlyOpBalance[month] = int(monthlyClBalance[month-1])
            monthlyClBalance[month] = int(monthlyOpBalance[month])
            if spendingProfile.get(month) != None:
                 monthlyClBalance[month] = int(monthlyClBalance[month] - spendingProfile.get(month))
            if additionalCapital.get(month) != None:
                monthlyClBalance[month] += int(additionalCapital.get(month))
        
    result = [monthlyOpBalance,monthlyClBalance]
    return result

        

def main():
    month = 'January'
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
    result = classH(month,year,fundValue,fProfile,interestClass,interest,spending,addContri,timeframe)
    return result
