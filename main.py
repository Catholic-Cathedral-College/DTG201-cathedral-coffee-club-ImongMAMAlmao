#adding imports
import time
def welcome():
  print("           ,-*'^'~*-.,_,.-*~  ☕𝒲𝐸𝐿𝒞O𝑀𝐸 𝒯O 𝒯𝐻𝐸 𝒢0𝐿𝒟𝐸𝒩 𝒞𝒜𝐹𝐸☕  ~*-.,_,.-*~'^'*-,")
  print("~~~~~~~~~*~*~~~,~~~~~~~~~,~~~~~~~~*~~,~~~~~~~~~.,~~~~**~~~~~~~~~,~~~~~,~~~~~~~~~~,~~~")
welcome()
time.sleep(1)
print("")
def menu():
  print("                      ]|I{•------»   ☕  𝑀𝐸𝒩𝒰  ☕   »------•{I|]")
  print("                               _________________________")
  print("                               |𝓕𝓵𝓪𝓽 𝔀𝓱𝓲𝓽𝓮(1) $3.00    |")
  print("                               |𝓒𝓪𝓹𝓹𝓾𝓬𝓬𝓲𝓷𝓸(2) $3.00    |")
  print("                               |𝓛𝓪𝓽𝓽𝓮(3)      $3.50     |")
  print("                               |𝓗𝓸𝓽 𝓒𝓱𝓸𝓬𝓸𝓵𝓪𝓽𝓮 (5) $4.00|")
  print("                               |________________________|")


name = input("what is your name?     ")

print(f"Hello {name} 𝒲𝐸𝐿𝒞O𝑀𝐸 𝒯O 𝒯𝐻𝐸 𝒢0𝐿𝒟𝐸𝒩 𝒞𝒜𝐹𝐸")
menu = input ('do you want to see the menu? yes or no?  :' )
if menu == str('yes'):
  func menu()