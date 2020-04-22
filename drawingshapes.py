def drawStars(num):
    for i in range(num):
        print("*",end=" ")
    print()

def menu():
    ###PRINT MENU HERE###
    choice = int(input("Please choose a shape: "))
    return choice
    

def drawSquare(length):
    ###USE drawStars TO PRINT A SQUARE OF CORRECT LENGTH###


def drawRectangle(length,height):
    ###USE drawStars TO PRINT A RECTANGLE OF CORRECT LENGTH AND HEIGHT###
 
    
def drawArrowhead(width):
    ###USE drawStars TO PRINT AN ARROWHEAD OF CORRECT LONGEST WIDTH###

    
def main():
    choice = menu()
    if(choice == 1):
        ###ASK USER FOR LENGTH###
        ###CALL drawSquare FUNCTION###
        
    elif(choice == 2):
        ###ASK USER FOR LENGTH###
        ###ASK USER FOR HEIGHT###
        ###CALL drawRectangle FUNCTION###
        
    elif(choice == 3):
        ###ASK USER FOR WIDTH###
        ###CALL drawArrowhead FUNCTION###
        
    
main()