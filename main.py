#adding imports
import time #imports time function
A = int("3")
B = float("3.50")
C = int("3")
D = int("4")
sugar = float("0.5")
total = 0
def order():
  orderlist =  {"A", "B", "C", "D"}
  total = int('0')
  order = input("what would you want to order? (please space your orders out)").upper().split()
  print("Your Order are ", order )
  if 'A' in order:
    total += A
  if 'B' in order:
    total += B
  if 'C' in order:
    total += C
  if 'D' in order:
    total += D
  print('your total is $',total)
  if order not in orderlist:
    print("pls order")
    

# i made my menu into a string variableso that i can call it again and again.
menu1 = "I•------»   ☕  𝑀𝐸𝒩𝒰  ☕   »------•I \n ________________________ \n |𝓕𝓵𝓪𝓽 𝔀𝓱𝓲𝓽𝓮(A) $3.00    | \n |𝓒𝓪𝓹𝓹𝓾𝓬𝓬𝓲𝓷𝓸(C) $3.00    | \n |𝓛𝓪𝓽𝓽𝓮(B)      $3.50    | \n |𝓗𝓸𝓽 𝓒𝓱𝓸𝓬𝓸𝓵𝓪𝓽𝓮 (D) $4.00| \n |_______________________|"
def welcome(): #it prints the welcometext at the beginning 
  print("           ,-*'^'~*-.,_,.-*~  ☕𝒲𝐸𝐿𝒞O𝑀𝐸 𝒯O 𝒯𝐻𝐸 𝒢0𝐿𝒟𝐸𝒩 𝒞𝒜𝐹𝐸☕  ~*-.,_,.-*~'^'*-,")
  print("~~~~~~~~~*~*~~~,~~~~~~~~~,~~~~~~~~*~~,~~~~~~~~~.,~~~~**~~~~~~~~~,~~~~~,~~~~~~~~~~,~~~")
welcome()

name = input("what is your name?     ")

print(f"Hello {name} 𝒲𝐸𝐿𝒞O𝑀𝐸 𝒯O 𝒯𝐻𝐸 𝒢0𝐿𝒟𝐸𝒩 𝒞𝒜𝐹𝐸")
def menu():
  menu = input('do you want to see the menu? yes or no?  :' )
  while menu != 'yes':
    menu = input ('do you want to see the menu? yes or no?  :' )
    if menu == 'yes':
      print(menu1)
      order()
    if menu == 'no':
      order()
time.sleep(1)
menu()