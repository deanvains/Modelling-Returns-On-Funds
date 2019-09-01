def ClassN():
    
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
    OutflowSpending = int(input ("Please enter spending: "))
    StartingMonth = input ("Please enter starting month: ")
    StartingYear = int(input ("Please enter starting year: "))
    EndingMonth = input ("Please enter ending month: ")
    EndingYear = int(input ("Please enter ending year: "))
    ChangeSpending = int(input ("Please enter new spending amount: "))
    ChangeSpendingMonth = input ("Please enter change month: ")
    ChangeSpendingYear = int(input ("Please enter change year: "))
    
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
        
        #Calculate when the spending amount change occurs.
        ChangeMonth = ((ChangeSpendingYear - StartingYear)*12) + monthDict[ChangeSpendingMonth]
        
        #For loop starting at the value of the starting month to the value of the upper limit of the loop.
        for x in range(StartingMonthValue, Upper+1):
            
            #Check if spending amount to be changed for this and ongoing months.
            if (x == ChangeMonth):
                OutflowSpending = ChangeSpending
            
            #Calculate the monthly balance.
            OpeningBalance = OpeningBalance - OutflowSpending
            
            print(x, "$ ", OpeningBalance)
