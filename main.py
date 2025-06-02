TOTAL_LINES = 3
MIN_BET = 1
MAX_BET = 100


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
      bet = input(f"What would you like to bet on each lines?  $")
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

   while True:
      bet = get_bet()
      total_bet = bet * lines

      if total_bet > balance:
         print(f"You do not have ${total_bet} to place a bet, your current balance is ${balance} !")
      else:
         break

   print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")

main()