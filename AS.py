
def kIsClicked(): 
    print("Character moves right ")
def hUsClikced():
    print("Charater moves left")

keepGoing = True
#boolean = 뭐냐면 TRUE 또는 False냐의 변수
while True:
    userInput = input("which number do you want to choose? (1~9) type 9 ")
    
    if userInput == "k":
        kIsClicked()
        
    elif userInput == "9":
        print("Finished")
        break
    else:
        break



