#Ayush Kadigari
#PD 8
#Election Assignment
print("The Wootton Thanks You For Tallying Our Election Data!")
print("******************************************************")
print("The TOP 4 Candidates for the Democratic nomination are:")
print("Joe Biden, Bernie Sanders, Elizabeth Warren & Kamala Harris")
#Staff votes

print("Enter number of Staff votes for Joe Biden")
bidStaff = int(input())

print("Enter number of Staff votes for Bernie Sanders") 
sanStaff = int(input())

print("Enter number of Staff votes for Elizabeth Warren") 
warStaff = int(input())

print("Enter number of Staff votes for Kamala Harris")
harStaff = int(input())

#Student Votes 
print("Enter number of Student votes for Joe Biden") 
bidStudent = int(input())

print("Enter number of Student votes for Bernie Sanders") 
sanStudent = int(input())

print("Enter number of Student votes for Elizabeth Warren")
warStudent = int(input()) 

print("Enter number of Student votes for Kamala Harris") 
harStudent = int(input())

#Calculation
print("*******************")
print("Wootton Votes :")
print("*******************")
#Percentages

total = (bidStaff+sanStaff+warStaff+harStaff)
bidPercent = round(((bidStaff+bidStudent)/total)*100,2)
sanPercent = round(((sanStaff+sanStudent)/total)*100,2)
warPercent = round(((warStaff+warStudent)/total)*100,2)
harPercent = round(((harStaff+harStudent)/total)*100,2)

print("Joe Biden:" , bidPercent,"%")
print("Bernie Sanders:" , sanPercent,"%")
print("Elizabeth Warren:" , warPercent,"%")
print("Kamala Harris:" , harPercent,"%")

