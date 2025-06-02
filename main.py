

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
         print("Please enter a number !!! ")      

   return amount

deposit()