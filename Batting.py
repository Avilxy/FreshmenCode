#Ayush Kadigari
#Sekaran
#PD 8
#Batting Average
print("================================================================")
print("Baseball Team Manager")
print("This program calculates the batting average for a player based")
print("on the player's official number of at bats and hits.")
print("===============================================================")

player = (input("Player's Name:"))
at_bats = float(input("Official number of at bats:"))
hits = float(input("Number of hits:"))

average = hits / at_bats
print("Batting Average is:" , average)