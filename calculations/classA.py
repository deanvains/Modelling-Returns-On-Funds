def calMonths(year1,year2,month1,month2):
    return int((year1-year2) * 12 +(month2-month1))

def operatingAccount (month,year,value,fprofile,intclass,interest,spending,recap,distribution,timeframe):
    
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
    recapital = recap
    yearlyCapDist = distribution
    
 
        
        
    monthlyOpBalance = {}
    monthlyClBalance = {}
    monthlyReturn = {}
    annualAMB = {}
            
        
    for month in range(0,timeFrame):
        if month == 0 and dateMonth == "December":
            monthlyOpBalance[month] = fundValue
            monthlyClBalance[month] = monthlyOpBalance[month]
            if spendingProfile.get(month) != None:
                 monthlyClBalance[month] = int(monthlyClBalance[month] - spendingProfile.get(month))
            if recapital.get(month) != None:
                monthlyClBalance[month] -= int(recapital.get(month))
            annualAMB[1] = int(monthlyOpBalance[month])   

        elif month == 0 and dateMonth != "December" :
            monthlyOpBalance[month] = fundValue
            monthlyClBalance[month] = int(monthlyOpBalance[month])
            if spendingProfile.get(month) != None:
                 monthlyClBalance[month] = int(monthlyClBalance[month] - spendingProfile.get(month))
            if recapital.get(month) != None:
                monthlyClBalance[month] -= int(recapital.get(month))
        
        elif month > 0 and ((monthDict[dateMonth] + month ) % 12) == 0:
            monthlyOpBalance[month] = monthlyClBalance[month-1]
            sum = 0
            sumAWB = 0
            if month < 12:
                for bal in range(month+1,0,-1):
                    print(monthlyOpBalance[month - bal + 1])
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
            if recapital.get(month) != None:
                monthlyClBalance[month] -= int(recapital.get(month))
            if yearlyCapDist[(monthDict[dateMonth] + month)/12] != None:
                monthlyClBalance[month] += int(yearlyCapDist.get((monthDict[dateMonth] + month)/12))

          
        else :
            monthlyOpBalance[month] = int(monthlyClBalance[month-1])
            monthlyClBalance[month] = int(monthlyOpBalance[month])
            if spendingProfile.get(month) != None:
                 monthlyClBalance[month] = int(monthlyClBalance[month] - spendingProfile.get(month))
            if recapital.get(month) != None:
                monthlyClBalance[month] -= int(recapital.get(month))
        
    for x,y in monthlyReturn.items():
        print(x,y)
    
    for x,y in monthlyOpBalance.items():
        print(x,y)
    for x,y in annualAMB.items():
        print(x,y)

        
def main():
    month = 'January'
    year = 2019
    fundValue = 500000
    fProfile = None
    interestClass = 'A'
    interest = 0.03
    #i and spendAmount will not included in parameters, I used it here to populate the dictionary required for spending,
    #in our project, form should have a variable that stores a dictionary that can be passed here
    i = 0
    spendAmount = 41500
    
    spending = {}
    while i != 48:
        spending[i] = spendAmount
        i += 1
        if i == 12:
            spendAmount = 42000
        if i == 24:
            spendAmount = 43000
        if i == 36:
            spendAmount = 44000
    
    recap = {29:10000}
    distribution = {1:507500,2:523608,3:556729,4:591636}
    timeframe = 48
    operatingAccount(month,year,fundValue,fProfile,interestClass,interest,spending,recap,distribution,timeframe)