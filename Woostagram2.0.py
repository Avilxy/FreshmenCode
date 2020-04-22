username = input("Enter Username:")
password = input("Enter Password:")

if (username not in ("HexBeetle75","JavaMan27","PetPet")):
     print("That Username" ,username ,"does not exsit")


if (username == "HexBeetle75" and password != "invasivespecies"):
    print("Sorry, wrong password!")
elif (username == "HexBeetle75" and password == "invasivespecies"):
    print("Welcome ", username , "!")

if (username == "JavaMan27" and password != "coder"):
    print("Sorry, wrong password!")
elif (username == "JavaMan27" and password == "coder"):
    print("Welcome ", username , "!")

    
if (username == "PetPet" and password != "particardi"):
    print("Sorry, wrong password!")
elif (username == "PetPet" and password == "particardi"):
    print("Welcome ", username , "!")

#By Ayush Kadigari