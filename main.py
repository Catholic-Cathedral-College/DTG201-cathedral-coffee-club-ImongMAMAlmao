#adding imports
import time #imports time function
A = int("3")
B = float("3.50")
C = int("3")
D = int("4")
E = int("3")
sugar = float("0.5")
total = 0
menu1 = "Iโข------ยป   โ  ๐๐ธ๐ฉ๐ฐ  โ   ยป------โขI \n ________________________ \n |๐๐ต๐ช๐ฝ ๐๐ฑ๐ฒ๐ฝ๐ฎ(A) $3.00    | \n |๐๐ช๐น๐น๐พ๐ฌ๐ฌ๐ฒ๐ท๐ธ(C) $3.00    | \n |๐๐ช๐ฝ๐ฝ๐ฎ(B)      $3.50    | \n |๐๐ธ๐ฝ ๐๐ฑ๐ธ๐ฌ๐ธ๐ต๐ช๐ฝ๐ฎ (D) $4.00| \n |๐๐ฎ๐ฌ๐ช๐ฏ (E)        $3.00 | \n |_______________________|"
orderlist = ["A" "B" "C" "D" "E"]

def order(): #this is the function to add the orders and mixed with the payment method and the receipt for the coffe maker

  #these are the prices of each drink
  A = int("3")
  B = float("3.50")
  C = int("3")
  D = int("4")
  E = int('3')
  total = float('0')
  receipt = str ( name + '\n You ordered : ')
  
  print("\n")
  orders = True
  #this is to ask the user what they want to order
  order = input(" \n what would you want to order? enter letters (please space your orders out)").upper().split()
         
  #these if statements are to determine what, how many and how much they ordered
  if 'A' in order:
    numbera = float(input("\n How many Flat White drinks do you want?"))
    A = numbera * A
    total += A
    lettera = str(numbera)
    
  if 'B' in order:
    
    numberb = float(input("\n How many Latte drinks do you want?"))
    B = numberb * B
    total += B
    letterb = str(numberb)
    
  if 'C' in order:
    numberc = float(input("\n How many Cappuccino drinks do you want?"))
    C = numberc * C
    total += C
    letterc = str(numberc)
    
  if 'D' in order:
    numberd = float(input("\n How many Hot Chocolate drinks do you want?"))
    D = numberd * D
    total += D
    letterd = str(numberd)

  if 'E' in order:
    numbere = float(input("\n How many Decaf drinks do you want?"))
    E = numbere * E
    total += E
    lettere = str(numbere)  
  
  print("\n")

  #this if statements is to ask the user whether they want extra sugar on their drink or not
  asukal = input("do you want sugar? Y/N?").upper().strip()
  
  if asukal == 'Y':
    total += sugar
    
  if asukal != 'Y':
    print("\n")
    print("ok!")


  #these printed strings is to tell users on what they ordered and how much they ordered in total $
  print("\n")
  print("Your Order are ", order )
  print('\n your total is $',total)
  print('your receipt is ', order , total)
  if total == '0':
    print("Thank you for coming")
  
  payment = input("are you paying with cash or card? \n").lower().strip()
  enough = True
  #this if statements is for the user when they are paying 
  if payment != 'card':  
    while enough:
      cash = float(input("how much money are you paying with? "))
      if cash == total:
        print("\n")
        print ("thank you")
        print("\n")
        enough = False
        
      if cash > total:
        change = cash - total
        print("\n")
        print ("this is your change : $", change)
        print("\n")
        print ("thank you")
        enough = False
        
      else:
        print("please pay the right amount.")
     

  if payment == 'card':
    print("please insert your card")
    pin = str(input('\n please enter your 4 digit pin.'))
    print('Thank you for orderin in ๐ข0๐ฟ๐๐ธ๐ฉ ๐๐๐น๐ธ')
  print('\n')
    
  # this if statements are to print the chosen drink and beside it is how many of the drinks they ordered
  if 'A' in order:
    receipt += (' Flat White ' + lettera +'\n')

  if 'B' in order:
    receipt += (' Latte ' + letterb +'\n')
  
  if 'C' in order:
    receipt += (' Cappuccino ' + letterc +'\n')

  if 'D' in order:
    receipt += (' Hot Chocolate ' + letterd +'\n')

  if 'E' in order:
    receipt += (' Decaf ' + lettere +'\n')

  print (receipt)
    


def menu(): #this function asks the user if they are ready to order

  valid = True
  while valid:
    menu = input ('do you want to see the menu? yes or no?  :' ).lower().strip()
    if menu == 'yes':
      print('\n')
      print(menu1)
      order()
      valid = False
    if menu == 'no':
      print("\n")
      order()
      valid = False
    #break
    

def welcome(): #it prints the welcometext at the beginning 
  print("           ,-*'^'~*-.,_,.-*~  โ๐ฒ๐ธ๐ฟ๐O๐๐ธ ๐ฏO ๐ฏ๐ป๐ธ ๐ข0๐ฟ๐๐ธ๐ฉ ๐๐๐น๐ธโ  ~*-.,_,.-*~'^'*-,")
  print("~~~~~~~~*~*~~~,~~~~~~~~~,~~~~~~~~*~~,~~~~~~~~~.,~~~~**~~~~~~~~~,~~~~~,~~~~~~~~~~,~~~")


while True:
  welcome()
  print("\n")
  print("\n")
  name = input("what is your name?     ")
  print("\n")
  print(f"Hello {name} ๐ฒ๐ธ๐ฟ๐O๐๐ธ ๐ฏO ๐ฏ๐ป๐ธ ๐ข0๐ฟ๐๐ธ๐ฉ ๐๐๐น๐ธ")
  print("\n")
  time.sleep(1)
  menu()
  continue

