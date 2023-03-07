from roulette import *
from placeBet import *
from gameFunctions import *

betType, betChoice, betAmount, bankRoll = placeBet()


while(True):
  bankRoll = makeRoll(betType, betChoice, betAmount, bankRoll)

  betType, betChoice, betAmount, bankRoll = placeBet(bankRoll)