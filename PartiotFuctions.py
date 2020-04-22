#Python Palace
#Allows a user to take a store menu and update it based on their input
def processSelection(optionlist):
  count = 0
  for i in optionlist:
    count = count + 1
    print(count,"\b)",i)

  modify = int(input("Would you like to 1)Add, 2)Remove, or 3)Change an item on this menu? "))

  if(modify == 1):
      addItem = input("What would you like to add? ")
      spot = int(input("Where would you like to add it? "))
      optionlist.insert(spot-1,addItem)
        
  elif(modify == 2):
      removeItem = input("What is the name of the item to remove? ")
      optionlist.remove(removeItem)
        
  else:
      spot = int(input("What is the number of the item you want to change? "))
      newItem = input("What is the name of the new item? ")
      optionlist[spot-1] = newItem
        
  #print new list
  count = 0
  for i in optionlist:
    count = count + 1
    print(count,"\b)",i)

#main function
def main():
  
    #create menu lists
    menuOptions = ["Sandwiches","Sides","Drinks"]
    sandwichList = ["Turkey","Tuna","Steak and Cheese","Grilled Chicken","BLT"]
    sideList = ["Fries","Chips","Sweet Potato Fries","Salad"]
    drinkList = ["Coffee","Tea","Water","Apple Juice","Orange Juice"]
    
    #print main menu items and ask user what they would like to change
    print("***MAIN MENU***")
    count = 0
    for i in menuOptions:
        count = count + 1
        print(count,"\b)",i)
    
    selection = int(input("What type of items would you like to edit? "))
    
    #if user chooses sandwiches:
    #print the list and allow them to pick whether to add, remove, or change
    if (selection == 1):
      processSelection(sandwichList);
    
    #if user chooses sides:
    #print the list and allow them to pick whether to add, remove, or change
    elif (selection == 2):
        processSelection(sideList);
    
    #if user chooses drinks:
    #print the list and allow them to pick whether to add, remove, or change
    else:
        processSelection(drinkList);

#tells the compiler to call the main function  
main()

#By Ayush Kadigari