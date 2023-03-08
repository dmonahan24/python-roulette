def placeBet(prevBankRoll=None):
    if prevBankRoll == None:
        bankRoll = input('Please enter the buy in amount or "Exit" to quit: ')
        if bankRoll == "Exit":
            quit()
        elif not bankRoll.isdigit():
            print('You have made an incorrect entry. Please enter a number greater than 0')
            bankRoll = 0
            placeBet(None)
        elif float(bankRoll) <= 0:
            print('You have made an incorrect entry. Please enter a number greater than 0')
            bankRoll = 0
            placeBet(None)
    elif prevBankRoll == 0:
        print('You have ran out of money.')
        bankRoll = input('Please enter a new buy in amount or "Exit" to quit: ')
        if bankRoll == "Exit":
            quit()
        elif not bankRoll.isdigit():
            print('You have made an incorrect entry. Please enter a number greater than 0')
            bankRoll = 0
            placeBet(None)
        elif float(bankRoll) <= 0:
            print('You have made an incorrect entry. Please enter a number greater than 0')
            bankRoll = 0
            placeBet(None)
    else:
        bankRoll = prevBankRoll
    
    betAmount = input('Please enter your bet amount or "Exit" to quit: ')
    if betAmount == "Exit":
        quit()
    #   Check to see if the bet ammount is valid
    elif not betAmount.isdigit():
        print('Error: You have bet an incorrect ammount. All bets must be more than 0.')
        betAmount = 0
        placeBet(bankRoll)
    elif float(betAmount) <= 0.0:
        print('Error: You have bet an incorrect ammount. All bets must be more than 0.')
        betAmount = 0
        placeBet(bankRoll)
    
    #   Check to see if there is enough money in the bank account
    if float(bankRoll) - float(betAmount) < 0.0:
        print('You do not have enough money in your bank account to bet this much.')
        placeBet(bankRoll)
    print('Bet type options "Number", "EvenOrOdd", "RedOrBlack", "Groups", or "LowHigh"')
    betType = input('Please enter a bet type or "Exit" to quit: ')
    if betType == "Number":
        betChoice = input("Please enter a number between -1 (00) and 36: ")
        return(betType, betChoice, betAmount, bankRoll)
    elif betType == "EvenOrOdd":
        betChoice = input('Please choose "Even" or "Odd": ')
        return(betType, betChoice, betAmount, bankRoll)
    elif betType == "RedOrBlack":
        betChoice = input('Please choose "Red" or "Black": ')
        return(betType, betChoice, betAmount, bankRoll)
    elif betType == "Groups":
        betChoice = input('Please enter "First" for 1-12, "Second" for 13-24, or "Third" for 25-36: ')
        return(betType, betChoice, betAmount, bankRoll)
    elif betType == "LowHigh":
        betChoice = input('Please enter "Low" for 1-18 or "High" for 19-36: ')
        return(betType, betChoice, betAmount, bankRoll)
    elif betType == "Exit":
        quit()
    else:
        print("You have made an incorrect choice")
        return(placeBet(bankRoll))