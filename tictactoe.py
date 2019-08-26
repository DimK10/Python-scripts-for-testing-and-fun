board = '''                   ||     ||
                 {6} ||  {7}  ||  {8}
               ____||_____||____
                   ||     ||
                 {3} ||  {4}  ||  {5}
               ____||_____||____
                   ||     ||
                 {0} ||  {1}  ||  {2}
                   ||     ||    
'''
bmem = [" " for i in range(9)]




#Check for valid input on X or O
def checkinputxo():
    while True:
        
        try:
            playerinput = str(input("Choose X or O: "))
            if playerinput == "X" or playerinput == "x":
                return "X"
            elif playerinput == "O" or playerinput == "o":
                return "O"
            else:
                print("I did not understand that. ENTER X OR O NOT ZERO !!!")
                continue
        except ValueError:
            print("I did not understand that. ENTER X OR O NOT ZERO !!!")
            continue
#Check for valid input on number, and for existing X or O
def checknumber(bmem):
    while True:
        
        try:
            playerinput = int(input("Choose between 1 and 9: "))
            if 1<=playerinput and playerinput<=9:
                if bmem[playerinput-1] == "X" or bmem[playerinput-1] == "O":
                    print("The number you gave corresponds to a position that is taken already")
                    continue
                else:
                    return playerinput - 1 
            else:
                print("Sorry i didn't understand that. Enter a number between 1 and 9!!!")
                continue
        except ValueError:
            print("Sorry i din't understand that. Enter a number between 1 and 9!!!")
            continue


    
#Check for victory or stalemate conditions
def checkvictorystalemate(bmem):
    
    
    if bmem[0]==bmem[1]==bmem[2]=="X" or bmem[3]==bmem[4]==bmem[5]=="X" or bmem[6]==bmem[7]==bmem[8]=="X"\
       or bmem[0]==bmem[3]==bmem[6]=="X" or bmem[1]==bmem[4]==bmem[7]=="X" or bmem[2]==bmem[5]==bmem[8]=="X"\
       or bmem[0]==bmem[4]==bmem[8]=="X" or bmem[2]==bmem[4]==bmem[6]=="X":
        return "X"
            
    elif bmem[0]==bmem[1]==bmem[2]=="O" or bmem[3]==bmem[4]==bmem[5]=="O" or bmem[6]==bmem[7]==bmem[8]=="O"\
       or bmem[0]==bmem[3]==bmem[6]=="O" or bmem[1]==bmem[4]==bmem[7]=="O" or bmem[2]==bmem[5]==bmem[8]=="O"\
       or bmem[0]==bmem[4]==bmem[8]=="O" or bmem[2]==bmem[4]==bmem[6]=="O":
        return "O"

    if not(" " in bmem):
        print("stalemate")
        return "stalemate"
def checkcontinue(bmem):
    while True:
        playerinput = str(input("Do you wish to play another game? Type Yes of No and hit enter "))
        try:
            if playerinput == "Yes" or playerinput == "yes" or playerinput == "YES":
               
                return True
            elif playerinput == "No" or playerinput == "no" or playerinput == "NO":
                return False
            else:
                print("Sorry i didnt understand that. Please type yes or no and hit enter")
                continue
        except ValueError:
            print("Sorry i didnt understand that. Please type yes or no and hit enter")
            continue
    
#Lets make this viable this time



while True:
    print("Welcome to tic tac toe")
    player1 = checkinputxo()
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    turns = 1
    while True:
        if turns % 2 == 1:
            print("Player1 turn")
            playerinput = checknumber(bmem)
            bmem[playerinput] = player1
            print("\n"*1000)
            print(board.format(bmem[0], bmem[1], bmem[2], bmem[3], bmem[4], bmem[5], bmem[6], bmem[7], bmem[8]))
            if player1 == checkvictorystalemate(bmem):
                print("Congratulations, player1 wins!")
                break
            elif checkvictorystalemate(bmem) == "stalemate":
                break

        else:
            
            print("Player2 turn")
            playerinput = checknumber(bmem)
            bmem[playerinput] = player2
            print("\n"*1000)
            print(board.format(bmem[0], bmem[1], bmem[2], bmem[3], bmem[4], bmem[5], bmem[6], bmem[7], bmem[8]))
            if player2 == checkvictorystalemate(bmem):
                print("Congratulations, player2 wins!")
                break
            elif checkvictorystalemate(bmem) == "stalemate":
                break
        turns += 1
    if checkcontinue(bmem) == True:
        bmem = [" " for i in range(9)]
        print("\n"*1000)
        continue
    else:
        break
