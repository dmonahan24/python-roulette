from placeBet import *
from gameFunctions import *

print("Welcome to Python Roulette")
betType, betChoice, betAmount, bankRoll = placeBet()

while(True):
  bankRoll = makeRoll(betType, betChoice, betAmount, bankRoll)

  betType, betChoice, betAmount, bankRoll = placeBet(bankRoll)