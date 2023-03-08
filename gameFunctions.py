import random
from placeBet import placeBet

black = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
red = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
second = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
third = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
high = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

#   determine if the roll was odd or even
def checkEvenOrOdd(rollResult):
    if rollResult in black:
        return('Odd')
    elif rollResult in red:
        return('Even')
    #   if the roll wasn't odd or even it landed on 0, or 00
    else:
        return(rollResult)
    
#   determine if the roll was odd or even
def checkRedOrBlack(rollResult):
    if rollResult in red:
        return('Red')
    elif rollResult in black:
        return('Black')
    #   if the roll wasn't red or black it landed on 0, or 00
    else:
        return('Green')

#   determine what group the roll was in
def checkGroup(rollResult):
    if rollResult in first:
        return('First')
    elif rollResult in second:
        return('Second')
    elif rollResult in third:
        return('Third')
    #   if the roll wasn't in a group it landed on 0, or 00
    else:
        return(rollResult)
    
#   determine if the roll was low or high
def checkLowHigh(rollResult):
    if rollResult in low:
        return('Low')
    elif rollResult in high:
        return('High')
    #   if the roll wasn't in a group it landed on 0, or 00
    else:
        return(rollResult)

#   lets roll the roulette wheel
def rollTheRouletteWheel():
    #   the picked bet must be an interger between -1 and 36      
    theRoll = random.randint(-1,36)
    print("\n\n--- Rolling the Wheel ---")
    print('The ball has landed on ' + checkRedOrBlack(theRoll) + ' ' + str(theRoll))
    return(theRoll)
      
    
def makeRoll(betType, betChoice, betAmount, bankRoll):
    #   begin the Straight roulette bet and game type
    if betType == 'Number':
            #   the picked bet must be an interger between -1 and 36
        if int(betChoice) < -1 or int(betChoice) > 36:
            print('Error: You have picked an incorrect bet, please roll again with a bet between -1 and 36 where 00 is represented as -1')
            return()
        else:
            theRoll = rollTheRouletteWheel()
            print('You bet the ball would land on '+str(betChoice))

            if theRoll == int(betChoice):
                print('*** You are a winner! ***')
                print('The payout is 35 to 1')
                payout = 35.0*float(betAmount)
                bankRoll = float(bankRoll) + payout
                print(str(payout) + ' has been added to your account')
                print('Your new account balance is ' + str(bankRoll))
                print('*** Please roll again! ***')
                return(bankRoll)
            else:
                print('You have lost')
                bankRoll = float(bankRoll) - float(betAmount)
                print('Your bet of ' + str(betAmount)+' has been removed from your account')
                print('Your new account balance is '+ str(bankRoll))
                print('--- Please roll again! ---')
                return(bankRoll)
    #   Begin a color choice game
    elif betType == 'RedOrBlack':
        if betChoice == 'Red' or betChoice == 'Black':

            rollColor = checkRedOrBlack(rollTheRouletteWheel())
            print('You bet the ball would land on ' + betChoice)

            if rollColor == betChoice:
                print('*** You are a winner! ***')
                print('The payout is 1 to 1')
                payout = 1.0*float(betAmount)
                bankRoll = float(bankRoll) + payout
                print(str(payout)+' has been added to your account')
                print('Your new account balance is '+str(bankRoll))
                print('*** Please roll again! ***')
                return(bankRoll)
            else:
                print('You have lost')
                bankRoll = float(bankRoll) - float(betAmount)
                print('Your bet of '+str(betAmount)+' has been removed from your account')
                print('Your new account balance is '+str(bankRoll))
                print('--- Please roll again! ---')
                return(bankRoll)
        else:
            print('Error: You have picked an incorrect color. Acceptable colors are Red and Black.')
            return(bankRoll)
    #   Begin an even or odd choice game
    elif betType == 'EvenOrOdd':
        if betChoice == 'Odd' or betChoice == 'Even':
            theRoll = rollTheRouletteWheel()
            evenOrOddResult = checkEvenOrOdd(theRoll)
            print('You bet the ball would land on ' + betChoice)

            if evenOrOddResult  == betChoice:
                print('*** You are a winner! ***')
                print('The payout is 1 to 1')
                payout = 1.0*float(betAmount)
                bankRoll = float(bankRoll) + payout
                print(str(payout)+' has been added to your account')
                print('Your new account balance is '+str(bankRoll))
                print('*** Please roll again! ***')
                return(bankRoll)
            else:
                print('You have lost')
                bankRoll = float(bankRoll) - float(betAmount)
                print('Your bet of '+str(betAmount)+' has been removed from your account')
                print('Your new account balance is '+str(bankRoll))
                print('--- Please roll again! ---')
                return(bankRoll)
        else:
            print('Error: You have picked an incorrect bet. Acceptable bets are Odd or Even.')
            return(bankRoll)
    
    #   Begin an groups game
    elif betType == 'Groups':
        if betChoice == 'First' or betChoice == 'Second' or betChoice == 'Third':
            theRoll = rollTheRouletteWheel()
            groupResult = checkGroup(theRoll)
            print('You bet the ball would land in the ' + betChoice + ' group.')

            if groupResult  == betChoice:
                print('*** You are a winner! ***')
                print('The payout is 2 to 1')
                payout = 2.0*float(betAmount)
                bankRoll = float(bankRoll) + payout
                print(str(payout)+' has been added to your account')
                print('Your new account balance is '+str(bankRoll))
                print('*** Please roll again! ***')
                return(bankRoll)
            else:
                print('You have lost')
                bankRoll = float(bankRoll) - float(betAmount)
                print('Your bet of '+str(betAmount)+' has been removed from your account')
                print('Your new account balance is '+str(bankRoll))
                print('--- Please roll again! ---')
                return(bankRoll)
        else:
            print('Error: You have picked an incorrect bet. Acceptable bets are First, Second, or Third.')
            return(bankRoll)
        
        #   Begin an lowHigh game
    elif betType == 'LowHigh':
        if betChoice == 'Low' or betChoice == 'High':
            theRoll = rollTheRouletteWheel()
            lowHighResult = checkLowHigh(theRoll)
            print('You bet the ball would land in the ' + betChoice + ' group.')

            if lowHighResult  == betChoice:
                print('*** You are a winner! ***')
                print('The payout is 1 to 1')
                payout = 1.0*float(betAmount)
                bankRoll = float(bankRoll) + payout
                print(str(payout)+' has been added to your account')
                print('Your new account balance is '+str(bankRoll))
                print('*** Please roll again! ***')
                return(bankRoll)
            else:
                print('You have lost')
                bankRoll = float(bankRoll) - float(betAmount)
                print('Your bet of '+str(betAmount)+' has been removed from your account')
                print('Your new account balance is '+str(bankRoll))
                print('--- Please roll again! ---')
                return(bankRoll)
        else:
            print('Error: You have picked an incorrect bet. Acceptable bets are First, Second, or Third.')
            return(bankRoll)
            

    #    You have chosen an incorrect betting game type            
    else:
        print('Error: Incorrect betting choice')
        print('Incorrect betting choice. Please choice: Straight, Color, EvenOdd, Thirds, LowHigh')
        return(bankRoll)


