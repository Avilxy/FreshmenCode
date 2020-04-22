
Item= int(input("Enter the Item Number:"))
paid= float(input("Enter the Amount paid:"))

if Item==1:
    price=1.25
elif Item==2:
    price=.75
elif Item==3:
    price=.9
elif Item==4:
    price=.75
elif Item==5:
    price=1.5
elif Item==6:
    price=.75
if paid > price:
    change = paid - price
    print("Thanks for buying Item", Item, "Your Change is" , change)
elif price > paid:
    more = price - paid
    print("PLease insert another", round(more,2), "$")
elif price == paid:
    print("Thank you for buying item", Item)

#By Ayush Kadigari