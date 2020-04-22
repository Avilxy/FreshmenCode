numbershirt = 0
priceshirt = 0

def Addshirts(numbershirt):
  print("ADD T-SHIRTS") n
  addshirt = int(input("Add how many shirt:"))
  numbershirt = numbershirt + addshirt
  priceshirt = priceshirt + addshirt* 10
  



#vieworder
def VIEWORDER():
  print("VIEW ORDER")
#renivetshirt
def RemoveshirtsfromOrder():
  print("Remove T-Shirts from Order")
#checkout
def checkout():
  print("checkout")

#entire program, if statements and ask user for what to do 
def main():
  
  print("My Great T-Shirt Store")
  
  option = int(input("1 to Add TShirts, 2 to Remove T-Shirts from Order, 3 to View Current Order, 4 to Checkout: "))

  if option == 1:
    Addshirts(numbershirt)

  elif option == 2:
    RemoveshirtsfromOrder()

  elif option == 3:
    VIEWORDER()
  else:
    checkout()
    #while user hasn't enter 4 , checkout then it will continue
  while option != 4: 
    option = int(input("1 to Add TShirts, 2 to Remove T-Shirts from Order, 3 to View Current Order, 4 to Checkout: "))
    if option == 1:
      Addshirts(numbershirt)

    elif option == 2:
      RemoveshirtsfromOrder()

    elif option == 3:
      VIEWORDER()
      #when user enters anything other than 1, 2, 3 then check out will appear and end the p  rogram, exit the loop.
  else:
    checkout()

main()

#By Ayush Kadigari