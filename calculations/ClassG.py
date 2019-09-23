def classG(month,year,value,fprofile,intclass,interest,donation,recap,distribution,timeframe):
    
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

    
    
    dateMonth = month.lower()
    dateYear = year
    fundValue = value
    fundProfile = fprofile
    interestClass = intclass
    interest = interest
    donation = donation
    recapital = recap
    distribution = distribution
    timeFrame = timeframe
    
    monthlyOpBalance = {}
    monthlyClBalance = {}
    monthlyCapDist = {}
    monthlyReturn = {}
    AWB3yr = {}
    annualAMB = {}
            
        
    for month in range(0,timeFrame *12 +1):
        if month == 0 and dateMonth == "December":
            monthlyOpBalance[month] = fundValue
            monthlyCapDist[month] = int(monthlyOpBalance[month] * float(distribution))
            monthlyReturn[month] = int(monthlyOpBalance[month] * float(interest))
            monthlyClBalance[month] = int(monthlyOpBalance[month] + monthlyReturn[month] - monthlyCapDist[month])
            if donation.get(month) != None:
                monthlyClBalance[month] += int(donation.get(month))
            if recapital.get(month) != None:
                monthlyClBalance[month] += int(recapital.get(month))
            annualAMB[1] = int(monthlyOpBalance[month])
            AWB3yr[1] = int(monthlyOpBalance[month])
            
        elif month == 0 and dateMonth != "December" :
            monthlyOpBalance[month] = fundValue
            monthlyClBalance[month] = int(monthlyOpBalance[month])
            if donation.get(month) != None:
                monthlyClBalance[month] += int(donation.get(month))
            if recapital.get(month) != None:
                monthlyClBalance[month] += int(recapital.get(month))
         
        elif month > 0 and ((monthDict[dateMonth] + month ) % 12) == 0:
            monthlyOpBalance[month] = monthlyClBalance[month-1]
            sum = 0
            sumAWB = 0
            if month < 12:
                for bal in range(month+1,0,-1):
                    sum += monthlyOpBalance[month - bal + 1]
                annualAMB[(monthDict[dateMonth] + month)/12] = int(sum / month)
                AWB3yr[(monthDict[dateMonth] + month)/12] = int(annualAMB[(monthDict[dateMonth] + month)/12])
            else :
                for bal in range(12,12-12,-1):
                    sum += monthlyOpBalance[month - bal+1]
                annualAMB[(monthDict[dateMonth] + month)/12] = int(sum / 12)
                if (monthDict[dateMonth] + month)/12 == 2:
                    for bal in range(2,0,-1):
                        sumAWB += annualAMB[bal]
                    AWB3yr[(monthDict[dateMonth] + month)/12] = int(sumAWB/2)
                    
                elif (monthDict[dateMonth] + month)/12 == 1:
                    AWB3yr[(monthDict[dateMonth] + month)/12] = int(annualAMB[(monthDict[dateMonth] + month)/12])
                else:
                    for bal in range(int((monthDict[dateMonth] + month)/12),int(((monthDict[dateMonth] + month)/12) - 3),-1):
                        sumAWB += annualAMB[bal]
                    AWB3yr[(monthDict[dateMonth] + month)/12] = int(sumAWB/3)
            
            
            monthlyReturn[month] =  int(annualAMB[(monthDict[dateMonth] + month)/12] * float(interest))
            monthlyCapDist[month] = int(AWB3yr[(monthDict[dateMonth] + month)/12] * float(distribution))
            monthlyClBalance[month] = int(monthlyOpBalance[month] + monthlyReturn[month] - monthlyCapDist[month])
            if donation.get(month) != None:
                monthlyClBalance[month] += int(donation.get(month))
            if recapital.get(month) != None:
                monthlyClBalance[month] += int(recapital.get(month))
        else :
            monthlyOpBalance[month] = int(monthlyClBalance[month-1])
            monthlyClBalance[month] = int(monthlyOpBalance[month])
            if donation.get(month) != None:
                monthlyClBalance[month] += int(donation.get(month))
            if recapital.get(month) != None:
                monthlyClBalance[month] += int(recapital.get(month))
                
    result = [monthlyOpBalance,monthlyClBalance]
    return result
    """for x,y in monthlyReturn.items():
        print(x,y)
    
    for x,y in monthlyOpBalance.items():
        print(x,y)
    for x,y in annualAMB.items():
        print(x,y)"""
            


def main():
    month = 'December'
    year = 2018
    fundValue = 10000000
    fProfile = None
    interestClass = 'E'
    interest = 0.08
    #dictionary of month with key value of donation
    donation = {18:1000000}
    recap = {30:10000}
    distribution = 0.05
    timeframe = 49
    result = classG(month,year,fundValue,fProfile,interestClass,interest,donation,recap,distribution,timeframe)
