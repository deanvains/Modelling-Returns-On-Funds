def ClassQ():
    
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
    
    OpeningBalance = int(input ("Please enter the opening balance: "))
    StartingMonth = input ("Please enter starting month: ")
    StartingYear = int(input ("Please enter starting year: "))
    EndingMonth = input ("Please enter ending month: ")
    EndingYear = int(input ("Please enter ending year: "))
    InterestRate = float(input ("Please enter an interest rate (%): "))
    
    #If the date entered by the user is incorrect, give an error message.
    if StartingMonth not in monthDict:
        print("Please enter a valid month.")
        
    else:
        #Search the month dictionary for the starting month value.
        StartingMonthValue = monthDict[StartingMonth]
        
        #Search the month dictionary for the ending month value.
        EndingMonthValue = monthDict[EndingMonth]
        
        #Calculate the upper limit of the for loop range.
        Upper = ((EndingYear - StartingYear)*12) + EndingMonthValue
        
        #Initialise the Annual Balance list with the opening balance.
        MonthlyBalance = [OpeningBalance]
        
        #For loop starting at the value of the starting month to the value of the upper limit of the loop.
        for x in range(StartingMonthValue, Upper+1):
            
            #If the month is the first December, calculate and add the interest earned to the monthly balance.
            #This is separate from the other interest calculations to take into account the fact that the starting month may not be January.
            if (x == 12):
                OpeningBalance = OpeningBalance + int((InterestRate/100*(sum(MonthlyBalance[:13-StartingMonthValue])/(13-StartingMonthValue)))/2)

            #If the month is December but not the first December, calculate and add the interest earned to the monthly balance.
            elif (x % 12 == 0 and x != 12):
                OpeningBalance = OpeningBalance + int((InterestRate/100*(sum(MonthlyBalance[x-12-StartingMonthValue+1:x-StartingMonthValue+1])/12))/2)
                
            #Append the total to the list.
            MonthlyBalance.append(OpeningBalance)
            
            print(x, "$ ", OpeningBalance)
