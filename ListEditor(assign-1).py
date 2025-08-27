UserList = []
def ContinueQues():
    Ques = input("Your opperation is Done! Do you wanna continue?(Y/N): ").upper()
    if Ques == "Y":
        return True
    elif Ques == "N":
        return False
    else:
        print("Please answer!")
        ContinueQues()
def ListChecker():
    if len(UserList) == 0:
        return False
    else:
        return True

while True: 
    print("Choose the command you want to do in your list: ")
    print("1- Add an item")
    print("2- Insert item in a specific index")
    print("3- Remove an item")
    print("4- Sort your list")
    print("5- Reverse your list")
    print("6- Show your list")
    print("7- Shutdown the app")

    choose = int(input("Choose from options(1, 2 ,3 ,4 , 5, 6 ,7): "))

    if choose == 1:
        adder = input("Write the item you wanna add: ")
        UserList.append(adder)
        ContinueQues()
        if ContinueQues() == False:
            break
    elif choose == 2:
        inserterVal = input("Write the item you wanna insert: ")
        inserterInd = int(input("Write the index: "))
        UserList.insert(inserterInd, inserterVal)
        ContinueQues()
        if ContinueQues() == False:
            break
    elif choose == 3:
        if ListChecker() == True:
            remover = input("Write the item you wanna remove: ")
            UserList.remove(remover)
        else:
            print("Please Add items to your list first!")
        ContinueQues()
        if ContinueQues() == False:
            break
    elif choose == 4:
        if ListChecker() == True:
            UserList.sort()
            print("Done! Your list is sorted")
        else:
            print("Please Add items to your list first!")
        ContinueQues()
        if ContinueQues() == False:
            break
    elif choose == 5:
        if ListChecker() == True:
            UserList.reverse()
            print("Done! Your list arrange is reversed")
        else:
            print("Please Add items to your list first!")
        ContinueQues()
        if ContinueQues() == False:
            break
    elif choose == 6:
        if len(UserList) == 0:
            print("Your list is empty! Please add some items")
        else:
            print(f"Your List = {UserList}")
        ContinueQues()
        if ContinueQues() == False:
            break
    elif choose == 7:
        print("Good bye! See you soon")
        break
    else:
        print("Please write a number from 1 to 5 ONLY!")
