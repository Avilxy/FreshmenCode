

print("PayCheck Calculator")
harStudent = int(input())
print(hours)

hourlypay = float(input("What is you hourly pay"))
print(hourlypay)

Exp = int(input("What is your weekley expenses:"))
GrossPay = (hours*hourlypay)
print("Paycheck Calculator")
print("Hours Worked:", + hours)
print("Hourly Pay:", + hourlypay)

GrossPay = (hours*hourlypay)
print("GrossPay", + GrossPay)

TaxRate=.18
print("Tax Rate: 18%")
print("Weekley Expenses:", Exp)

taxAmount = GrossPay * TaxRate
print("Tax Amount:", + taxAmount)
TakeHomePay=GrossPay - taxAmount
print("Take home pay:", + TakeHomePay)

if TakeHomePay <= Exp:
    print("You need to get a secound job!")
else:
    print("You do not need to get a secound job!")

#By Ayush Kadigari
