MAX_BET = 100
MIN_BET = 1
TOTAL_LINES = 3


def deposit():
   while True:
      amount = input("Do you want to add amount?  $")
      if amount.isdigit():
         amount = int(amount)
         if amount > 0:
            break
         else:
            print("Enter a amount greater than 0 !!! ")
      else:
         print("Please enter a NUMBER !!! ")      
   return amount



def get_lines():
   while True:
      lines = input("Enter the numbers of lines you want to bet on (1 - " + str(TOTAL_LINES) + ")  ")
      if lines.isdigit():
         lines = int(lines)
         if 1 <= lines <= TOTAL_LINES:
            break
         else:
            print(f"Enter a number between (1 - {TOTAL_LINES})  ")
      else:
         print("Please enter a NUMBER !!")   
   return lines


def get_bet():
   while True:
      bet = input(f"Would you like to place a bet?  $")
      if bet.isdigit():
         bet = int(bet)
         if MIN_BET <= bet <= MAX_BET:
            break
         else:
            print(f"Please enter vaild amount between ${MIN_BET} - ${MAX_BET}  !!")
      else:
         print("Please enter a NUMBER !!")      
   return bet



def main():
   balance = deposit()
   lines = get_lines()
   bet = get_bet()

   print(balance)
   print(lines)
   print(bet)

main()