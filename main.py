import random

TOTAL_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbols_list = {
   "🍇" : 2,
   "🧁" : 4,
   "🍌" : 6,
   "🍭" : 8 
}


symbols_values = {
   "🍇" : 8,
   "🧁" : 6,
   "🍌" : 4,
   "🍭" : 2 
}


def get_winnings(columns, lines, bet, values):
   winnings = 0
   for line in range(lines):
      check = columns[0][line]
      for col in columns:
         check_symbol = col[line]
         if check != check_symbol:
            break
      else:
         winnings += values[check] * bet
   
   return winnings         


def get_slot_spin(rows, cols, symbols):
   all_symbols = []
   for a, b in symbols.items():
      for _ in range(b):
         all_symbols.append(a)

   columns = []
   for _ in range(cols):
      column = []
      current_symbols = all_symbols[:]
      for _ in range(rows):
         value = random.choice(current_symbols)
         current_symbols.remove(value)
         column.append(value)

      columns.append(column)

   return columns


def print_slot(columns):
   for row in range(len(columns[0])):
      for i, col in enumerate(columns):
         if i != len(columns) - 1:
            print(col[row], end=" | ")
         else:
            print(col[row], end="")
      print()      

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


def game(balance):
   lines = get_lines()

   while True:
      bet = get_bet()
      total_bet = bet * lines

      if total_bet > balance:
         print(f"You do not have ${total_bet} to place a bet, your current balance is ${balance} !")
      else:
         break

   print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}")
   get = get_slot_spin(ROWS, COLS, symbols_list)
   print_slot(get)
   
   winning = get_winnings(get, lines, bet, symbols_values)
   print(f"You won $ {winning} ")

   return winning - total_bet


def main():
   balance = deposit()
   while True:
      print(f"Your current balance is ${balance}.")
      play = input(f"Press enter to play (press 'q' to quit)  ")
      if play == "q":
         break
      balance += game(balance)
   
   print()
   print()
   print(f"Thanks for playing !!! You left with ${balance}")
   print()
   print()

main()