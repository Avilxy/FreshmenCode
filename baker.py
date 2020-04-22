#Ayush Kadigari
#Sekaran
#PD 8
#Patriot Bakery
flavor = ['Chocalate','vanilla','funfetti','StrawBerry','Spice','Lemon']
print(flavor)
print("Enter your favorite flavor:(1-6)")
favflavor = int(input())
print(flavor[favflavor-1])
print("The fruit flavors are:", flavor[4], "and", flavor[5])
print("Please enter the item you would like to remove : (1-6)")
badflavor = int(input())
del flavor[badflavor-1]
print(flavor)
print("Please enter in a new flavor for the bakery:")
newflavor = input()
flavor.append(newflavor)
print(flavor)