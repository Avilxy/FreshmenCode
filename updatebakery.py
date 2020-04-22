
menuOptions = ["Cupcakes , Cookies, Drinks"]
cupcakesList = ["Chocolate, Vanilla, Funfetti, Red Velvet, Pumpkin Spice"]
cookiesList = ["Chocolate Chip, Oatmeal Raisin, Snickerdoodle, Peanut Butter"]
drinkList = ["Coffee, Tea, “Water, Apple Juice, Orange Juice"]
#Prints out main menu options
print ('***MAIN MENU***')
for i in menuOptions:
 print(i)
option1 = int(input("What type of items would you like to edit? 1,2,3: "))
#the options
if option1 == 1 or 2 or 3:
    realnum = option1 - 1
print(menuOptions[realnum])
if option1 == 1:
  for j in cupcakesList:
    print(j)
elif option1 == 2:
  for j in cookiesList:
    print(j)
elif option1 == 3:
  for j in drinkList:
    print (j)
#Options for Adding, Removing, or Changing
tochange = int(input('Would you like to 1)add, 2)remove, 3)Change an item on this menu?: '))
#Adding
if tochange == 1:
  add_item = str(input("What is the item you would like to add?: "))
  insert_area = int(input('where would you like to add the item in the menu?: '))
  if option1 == 1:
   cupcakesList.insert(insert_area-1, add_item)
   if len(cupcakesList) > 10:
    print("ERROR. Too many items.")
   else:
    for l in cupcakesList:
      print (l)
    print('Your menu has been successfully updated.')
#the section above lets you add items to the cupcake list and regulate it
  elif option1 == 2:
    cookiesList.insert(insert_area-1, add_item)
    if len(cookiesList) > 7:
      print ("ERROR. Too many items.")
    else:
      for l in cookiesList:
        print (l)
      print("Your menu has been successfully updated.")
#the section above is to add to the cookie list and regulate it
  elif option1 == 3:
    drinkList.insert(insert_area-1, add_item)
    if len(drinkList)>5:
      print("ERROR. Too many items.")
    else:
      for l in drinkList:
        print (l)
      print("Your menu has been succesfully updated.")
#this section above is to add items to the drink list and regulate it
#Removing
elif tochange == 2:
  remove_item = str(input("What is the name of the item you want to remove?:" ))
  if option1 == 1:
    cupcakesList.remove(remove_item)
    for m in cupcakesList:
      print (m)
#this section above is to remove items from the cupcake list
  elif option1 == 2:
    cookiesList.remove(remove_item)
    for m in cookiesList:
      print (m)
#this  section above is to remove items from the cookie list
  elif option1 == 3:
    drinkList.remove(remove_item)
    for m in drinkList:
      print (m)
  print("Your menu has been succesfully updated.")
#this section above is to remove items from the drink list
#Changing
elif tochange == 3:
  change_item = int(input("What is the number of the item you want to change?: "))
  changenum = change_item - 1
  newitemname = str(input("What is the name of the new item?: "))
  if option1 == 1:
    cupcakesList[changenum] = newitemname
    for n in cupcakesList:
      print (n)
#this section above lets you change items in the cupcake menu
  elif option1 == 2:
    cookiesList[changenum] = newitemname
    for m in cookiesList:
      print (m)
#this section above is to change items in the cookie menu
  elif option1 == 3:
    drinkList[changenum] = newitemname
    for m in drinkList:
      print (m)
#this section above is to change items in the drink menu

#By Ayush Kadigari