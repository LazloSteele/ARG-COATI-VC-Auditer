import datetime
import random

def getDate():
    month = 00
    day = 00
    year = 0000
    proceed = "False"

    while(month > 12 or month < 1):
        month = int(input("Please enter the month with no leading zeroes (ie. 3 = March, 11 = November): "))
        if(month > 12 and month < 1):
            print("That doesn't seem like a valid month. Please ensure your entry is a 2 digit decimal from 01-12.")
    print("Thanks!\n")

    dayMax = 0
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        dayMax = 31
    elif(month == 2):
        dayMax == 28
    else:
        dayMax == 30

    while(day > dayMax or day < 1):
        day = int(input("Please enter the day of the month in two decimal format (ie. 23 = the 23rd of the month): "))
    print("Groovy!\n")
    
    year = int(input("Now please enter the year in four decimal format as in: 2021 -or- 1975: "))

    date = datetime.date(year, month, day)

    while(proceed != "True"):
        print("The chosen date is: " + date.strftime("%m/%d/%y"))

        correct = input("Is this correct [Y/N]: ")

        if(correct == "y" or correct == "yes"):
            print("\nFabulous. Let's proceed.\n")
            proceed = "True"  
            return date

        elif(correct == "n" or correct == "no"):
            print("\nOh, I'm sorry. Let's fix that!\n")
            print("This feature is still in the works...")

        else:
            print("\nHmmm... I don't understand that.\n")

class VCRule():
    
    def __init__(self, start, end, rev, use, tipsShare, comOps):
        self.startDate = start
        self.endDate = end
        self.revShare = rev
        self.useFee = use
        self.tips = tipsShare
        self.commonOps = comOps

class pod:

    def __init__(self, name, sales, rules):
        self.name = name
        self.sales = sales
        self.rules = rules

    def getRules(self, date):
        for rule in self.rules:
            if(date >= rule.startDate and date < rule.endDate):
                return rule

    def getSales(self, date):
        return(self.sales[date])

def MonthlyReport(sales, rules):
    revShare = sales * rules.revShare
    commonOps = sales * rules.commonOps
    useFee = sales * rules.useFee

    totalFees = revShare + commonOps + useFee
    venderComp = sales - totalFees

    return([sales, totalFees, venderComp])

def audit(pods,startDate,endDate):

    for chefPartner in pods:
        print(chefPartner.name)
        currentDate = startDate
        salesMatrix = []
        monthlyReportMatrix = []
        monthlySales = 0
        currentRules = VCRule(datetime.date(1900,9,1),startDate,0.15,.1,0.15,.1)
        while(currentDate <= endDate):
            currentSales = chefPartner.getSales(currentDate)
            print(currentDate.strftime("%m/%d/%y") + ": $" + str(currentSales))
            if(chefPartner.getRules(currentDate) == True):
                currentRules = chefPartner.getRules(currentDate)
            tomorrow = currentDate + datetime.timedelta(1.0)
            if(tomorrow.day == 1):
                monthlyReportMatrix.append(MonthlyReport(monthlySales, currentRules))
                print("$" + str(monthlySales))
                monthlySales = 0
            monthlySales += currentSales
            #salesMatrix.append((currentDate, currentSales, currentRules.revShare, currentRules.useFee, currentRules.tips, currentRules.commonOps))    
            currentDate = tomorrow


        print(chefPartner.name + ": ")
        print("sales, totalFees, venderComp")
        for report in monthlyReportMatrix:
            print(str(report))

def main():

    print("Hello Monica, this program is written to assist in VC audits for ARG going forward. Included are the VC rules as understood by Lazlo by Nov. 10, 2021.\n")
    print("First things first let's get that starting date huh?\n")

    startDate = getDate()

    print("Now let's get that ending date to determine the date range we are auditing.\n")

    endDate = getDate()

#    startDate = datetime.date(2021,1,1)
#    endDate = datetime.date(2021,12,31)

    testSales = dict()
    i = startDate
    while i <= endDate:
        testSales[i] = random.randint(0,14000)
        i+= datetime.timedelta(1)

    testRule = VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)

    twoSuns = pod("Two Suns", testSales, [testRule])
    paleta = pod("Paleta Bar", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,2,12),0.15,.1,0.15,.1),VCRule(datetime.date(2021,2,13),datetime.date(2021,12,31),0.20,.2,0.2,.2)])
    xoxo = pod("XOXO", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])
    equilibrium = pod("Equilibrium", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])    
    sammich = pod("Sammich Shack", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])
    slowDownz = pod("Slow Downz", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])
    haoles = pod("Haoles", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])
    luchals = pod("Luchals", testSales,[VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])
    anju = pod("Anju", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])
    rival = pod("Rival Bar", testSales, [VCRule(datetime.date(2020,9,1),datetime.date(2021,12,31),0.15,.1,0.1,0.15)])
    ephemera = pod("Ephemera", testSales,  [VCRule(datetime.date(2020,9,1),datetime.date(2021,2,12),0.15,.1,0.15,.1),VCRule(datetime.date(2021,2,13),datetime.date(2021,12,31),0.20,.2,0.2,.2)])

    podsAudited = [twoSuns,paleta,xoxo,equilibrium,sammich,slowDownz,haoles,luchals,anju,rival,ephemera]

    if(endDate > startDate):
        print("Ok, we are looking at sales for " + startDate.strftime("%m/%d/%y") + " to " + endDate.strftime("%m/%d/%y") + " for the pods: ")
        for i in podsAudited:
            print(i.name)
        print("\n")
        audit(podsAudited,startDate,endDate)
    elif(endDate < startDate):
        print("Woopsie, that doesn't seem like a valid date range. Please exit and try again.")

main()