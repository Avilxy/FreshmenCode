#Task Project
#We created a simulation game allowing people to make there own choices and deciding what options leading to beat the game.
import time
# ^^^ this import are timing mechanism allowing an iteration to happen between sentences

def main():
#Main function for the whole program 

  print("Welcome to the game of Jumanji!")
  #Presents with the creator of the game
  print("How to play: You will be placed in a world where you will make choices that will affect your story Press 1 for option 1 or 2 for option 2")
  print("=====================================")
  name = str(input("What is your name? "))
  #Shows Name and age at the bottom we have the introduction
  print("Hello", name, "! Welcome to Jumanji! You must survive the world of mother nature and explore the hidden jewels of Jumanji!" "\n" "You will be assigned a task to find a specific object in a location you choose.""\n" "Choose wrong, you die.""\n" "Choose right, you move on. Good Luck!!!" "\n""Your survival determines the outcome of this world. The fate of Jumanji is in your hands. ")
  time.sleep(4)
  #At the bottom it shows a short sentence of location is the something as well as a process option where it creates a process to the if and elif statements
  loc=location()
  print("you have enterd option :"+ str(loc))
  processLocation(loc)
#
def location():
    loc = int(input("Where would you like to begin your journey?""\n""1.Amazon Forest""\n""2.Sahara Desert""\n""Enter your option:"))
    return loc
#Shows the list of options you can choose to create your story

def processLocation(choice):
  if choice == 1:
    amazonforest()
  elif choice == 2:
    saharadesert()
  else:
    invalid()
#processLocation presents the if, elif and else either choose sahara or amazon.

def invalid():
  print ("Please choose a valid number, either 1.the Amazon Forest or 2.the Sahra Desert")
  loc=location()
  processLocation(loc)
#If person does not make an option then 

#_____________________________________________________

#Beginning of the amazon forest code
def amazonforest():
  print(" ")
  print("Great!!! We are off to the Amazon rainforest")
  time.sleep(2)
  print("You have arrived to the Amazon Forest..... ")
  time.sleep(2)
  #the time.sleep gives a break in the code
  print("You have been deployed somewhere deep in the Amazon rainforest." "\n" "Your first mission is to find the Amazon river!!!")
  ama1=amazonone() 
  processAmazon1(ama1)
#If the user enter in the amazon option

def amazonone():
  print(" ")
  option= int(input("You find a small creek, but it is infested with pirahnas. What do you do:""\n""1.Follow it""\n""2.Jump in it?""\n""Enter your option:"))
  return option
#this is the code for amazonone
#it tells us the upcoming story

def diedRestart():
  print("You died!!!")
  time.sleep(1)
  answer = (input("Game Over!\n\nEnter 'N' for New Game:"))
  if answer == ("N"):
    print("")   
    main()
  else: 
    print("Good Bye!!!")
    #this is the code for the restart of the function

def amazonfollowriver():
  print("Nice job! You chose correctly!!! ""\n""Now we are off to second mission!!!")
  time.sleep(2)
  print("")   
  choice=amazontwo()
  processAmazon2(choice)
  #this is the code for when the selected the correct option of following the river

def amazonjumpriver():
  diedRestart()
  #this is a restart when they get it wrong

def processAmazon1(choice):
  if choice == 1:
    amazonfollowriver()
  elif choice == 2:
    amazonjumpriver()
    #this is a restart when they get it wrong

def amazontwo():  
  print("Now that you have followed the river, we have reached a gaint mountain. ""\n""As you climb up the mountain, there is a gaint jaguar prowling.Do you")
  option = int(input("1.Use your anti-jaguar repellent or ""\n""2.Rub steak sauce all over your face to attract the jaguar?""\n""Enter your option:"))
  return option
#this is the code for amazontwo
#it tells us the upcoming story

def processAmazon2(choice):
  if choice == 1:
    amazon2repellent()
  elif choice == 2:
    amazon2steaksauce()#this is a restart when they get it wrong

def amazon2repellent():
  print("Great, you picked the right choice! The jaguar ran away because of the correct option you chose. ")
  choice=amazonthree()
  processAmazon3(choice)#this is a restart when they get it wrong

def amazon2steaksauce():
  diedRestart()
#each of these def functions relate to amazon two
#they help us learn more

def amazonthree():
  time.sleep(3)
  print(" ")
  print("Now that you have successfully, repelled the jaguar, you must complete your main mission.""\n""Your last mission is to find and take a picture of a three toed sloth.")
  time.sleep(2)
  option = int(input(("OOH!!! Do you hear that!?! It is a three toed sloth! Do you want to ....""\n""1.Take a picture or ""\n""2.Scare it off?""\n""Enter your option:")))
  return option
#this is the code for amazonthree
#it tells us the upcoming story

def amazon3Picture():
  print("YAY! You got a picture of the three toed sloth! You mission is done! You have been rewarded 1 million dollars!")
  amazonFinish()#this is a restart when they get it wrong

def amazon3ScareIt():
  print("Uh oh, that is wrong. Please start over from the begininng!")
  diedRestart()
  #this is a restart when they get it wrong

def amazonFinish():
  print("==================")
  print("Congratulations")
  time.sleep(2)
  print("You Have Succesfully completed the demo of our game Let us Know how thing")
  time.sleep(2)
  print("I hoped you enjoyed :)")
#this is the finising code for when you have amazon 
def processAmazon3(choice):
  if choice == 1:
    amazon3Picture()
  elif choice == 2:
    amazon3ScareIt()
#Amazon3 process option  

#________________________________________________

#Beginning of the sahara part of the story 
def saharadesert():
  print(" ")
  print("Alright, the Sahara it is!")
  time.sleep(2)
  print("You enter the Sahara desert..... ")
  time.sleep(2)
  print("Welcome to the Sahara desert! THe most dangerous desert on planet Earth!")
  time.sleep(2)
  choice=saharaone()
  processSahara1(choice)
  
  print("")  
  #this is the code for saharadesert
  #it tells us the upcoming story
  
def saharaone():
  print(" ")
  choice = int(input("Your position is 58 miles west of the Nile river. What do you do: ""\n""1.Go 58 miles east""\n""2.Go 58 miles west?""\n""Enter your option:"))
  return choice
#this is the code for saharaone"\n""Enter your option:"
#it tells us the upcoming story

def processSahara1(choice):
  if choice == 1:
    sahara58east() 
    #this is the code for the process of sahara option1
  elif choice == 2:
    sahara58west()
#processOption for the sahara desert 

def sahara58west():
  print("You died from lack of water")
  time.sleep(2)
  diedRestart()
  #this is a restart when they get it wrong

def sahara58east():
  print("Correct choice! Now you are in the Nile!")
  choice=saharatwo()
  processSahara2(choice)
  #this is a restart when they get it wrong

def saharatwo():
  print(" ")
  option = int(input("Your next mission is to find Lake Victoria, the source of the Nile.""\n""Rivers generally flow uphill to downhill. You cannot walk along the coast because it is too hot and dangerous.""\n""Therefore you will need to travel  by water. What do you do: ""\n""1.Buy a sturdy raft from the locals ""\n""2.Swim uphill the Nile towards its source?""\n""Enter your option:"))
  print(" ")
  return option
#list for sahara part of the sahara story
  
def processSahara2(choice):
  if choice == 1:
    saharasturdyraft()
  elif choice == 2:
    saharaswimuphill()
   #this is the code for saharadesert
   #it tells us the upcoming story

def saharasturdyraft():
  print("GOOD! Getting a raft is the correct option!")
  time.sleep(2)
  choice=saharathree()
  processSahara3(choice)
  #this is the code for the sturdy raft that was chosen

def saharaswimuphill():
  diedRestart()
  #this is a restart when they get it wrong

def saharathree():
  print(" ")
  print("Great job! You have made it really far! Your last mission is to collect the rare plant Pelargonium culallatum also known as wild malva. It is a pink-ish plant that releases odor.""\n""There is another species of plant that mimics the wild malva. However this faker plant, ""\n""while also producing terrible odors, is distinguished by its vibrant red colors.")
  time.sleep(4)
  print("Ewww! What is that smell? You smell something terrible!")
  time.sleep(2)
  print("As you walk further, you see pink plants and red plants!")
  option = int(input("What do you do:""\n""1.Choose the pink plants ""\n""2.Choose the red plants""\n""Enter your option:"))
  print(" ")
  return option
 #this is the code for saharathree
#it tells us the upcoming story

def processSahara3(choice):
  if choice == 1:
    sahara3pinkplants()
  elif choice == 2:
    sahara3redplants()
#processOption for the sahara3 either you can choose red plants or pink plants 

def sahara3pinkplants():
  time.sleep(2)
  print(' ')
  print("Yea! That is correct! You got the rare wild malva plants! You have been congratulated 1 million dollars!")
  #Sahar3 pinkplants code
  saharafinish()
#up here is the def function for the end title 

def saharafinish():
  time.sleep(2)
  print(" ")
  print("==================")
  print("Congratulations")
  time.sleep(2)
  print("You Have Succesfully completed the demo of our game ")
  time.sleep(2)
  print("I hoped you enjoyed :)")
#if the user has finish the game it will present the end title 

#this is a restart when they get it wrong
def sahara3redplants():
  print(" ")
  print("Nope, you died! Please start over!")
  diedRestart()
#this is a restart when they get it wrong


main()
#this sequence gives us more about the final parts

#By Ayush Kadigari