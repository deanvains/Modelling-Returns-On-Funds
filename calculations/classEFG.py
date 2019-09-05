def ClassEFG():
    
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
    
    
    dateMonth = input("Please enter Month, January to December")
    dateYear = input("Please input Year")
    fundValue = int(input("Please enter Fund Value"))
    fundProfile = input("Please enter Fund Profile, 1 for Lump Sum, 2 for instalments over a period")
    interestClass = input("Please enter Interest Class, E,F,G")
    interest = float(input("Please enter LTP returns"))
    
    addtionalDonation = int(input("Any additional Donation? 1 for yea, 2 for nah"))
    donation = {}
    while addtionalDonation == 1:
        amountDonated = float(input("Enter Amount To Be Donated"))
        monthDonated = int(input("Enter Months After Opening of Fund Where Donations Occur"))
        donation[monthDonated] = amountDonated
        addtionalDonation = int(input("Any additional Donation? 1 for yea, 2 for nah"))
        
    reCap = int(input("1 for adhoc Recap, 2 for End Year"))
    recapital = {}
    while reCap == 1:
        amountRecap = float(input("Enter Amount To Be Recapitalized"))
        monthRecap = int(input("Enter Months After Opening of Fund Where Recapitalization Occur"))
        recapital[monthRecap] = amountRecap
        reCap = int(input("Any more Recap? 1 for yeah, 2 for nah"))

    
    distribution = 0
    if interestClass == 'E':
        distribution = 0.05
    elif interestClass == 'F':
        distribution = float(0)
    else:
        distribution = float(input("Please enter custom distribution"))
        
    spendingProfile = input("Please enter Spending Profile")
    timeFrame = int(input("Please enter a timeframe, How many months"))
    monthlyOpBalance = {}
    monthlyClBalance = {}
    monthlyCapDist = {}
    monthlyReturn = {}
    AWB3yr = {}
    annualAMB = {}
            
        
    for month in range(0,timeFrame+1):
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
                    print((monthDict[dateMonth] + month)/12)
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
        
    for x,y in monthlyReturn.items():
        print(x,y)
    
    for x,y in monthlyOpBalance.items():
        print(x,y)
    for x,y in annualAMB.items():
        print(x,y)
            


     
     
        
        
    
    
    
    