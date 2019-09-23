def findDec(startMonth):
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

     #Get the int equivalence of starting Month
     intMonth = monthDict[startMonth.lower()]
     
     return 12 - intMonth
    