from pyfiglet import Figlet
text1="you won plear1"
text2="you won plear2"
def show():
    for satr in game_board :
        for sotoon in satr :
            print(sotoon,end=" ")
        print()
def chek_plyer1():
    if game_board[0][0]=="x"and game_board[0][1]=="x"and game_board[0][2]=="x":
        print(text1)
    elif game_board[0][0]=="x"and game_board[1][1]=="x"and game_board[2][2]=="x":
        print(text1)
    elif game_board[0][2]=="x"and game_board[1][1]=="x"and game_board[2][0]=="x":
        print(text1)
    elif game_board[0][0]=="x"and game_board[1][0]=="x" and game_board[2][0]=="x":
        print(text1)
    elif game_board[1][0]=="x"and game_board[1][1]=="x"and game_board[1][2]=="x":
        print(text1)
    elif game_board[2][0]=="x"and game_board[2][1]=="x"and game_board[2][2]=="x":
        print(text1)
    elif game_board[0][1]=="x"and game_board[1][1]=="x"and game_board[2][1]=="x":
        print(text1)
    elif game_board[0][2]=="x"and game_board[1][2]=="x"and game_board[2][2]=="x":
        print(text1)
def chek_plyer2():
    if game_board[0][0]=="o"and game_board[0][1]=="o"and game_board[0][2]=="o":
        print(text2)
    elif game_board[0][0]=="o"and game_board[1][1]=="o"and game_board[2][2]=="o":
        print(text2)
    elif game_board[0][2]=="o"and game_board[1][1]=="o"and game_board[2][0]=="o":
        print(text2)
    elif game_board[0][0]=="o"and game_board[1][0]=="o" and game_board[2][0]=="o":
        print(text2)
    elif game_board[1][0]=="o"and game_board[1][1]=="o"and game_board[1][2]=="o":
        print(text2)
    elif game_board[2][0]=="o"and game_board[2][1]=="o"and game_board[2][2]=="o":
        print(text2)
    elif game_board[0][1]=="o"and game_board[1][1]=="o"and game_board[2][1]=="o":
        print(text2)
    elif game_board[0][2]=="o"and game_board[1][2]=="o"and game_board[2][2]=="o":
        print(text2)
t = Figlet(font='slant')
print(t.renderText("Tic Tac Toe"))
game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]
show()
while True:
    #plyer1
    print("plyer1")
    while True:
        satr=int(input("Enter a number for satr:"))
        sotoon=int(input("Enter a number for sotoon:"))
        if 0 <= satr <3 and 0 <= sotoon < 3 : 
            if game_board[satr][sotoon] == "-" :
                game_board[satr][sotoon] = "x"
                show()
                chek_plyer1()
                break
            elif "-" not in game_board[0]and"-" not in  game_board[1] and "-" not in game_board[2]:
                print("finish")
                break
            else:
                print("baiad ie khone dige antekhab koni in khone pore")
                satr=int(input("Enter a number for satr:"))
                sotoon=int(input("Enter a number for sotoon:"))
                if 0 <= satr <3 and 0 <= sotoon < 3 : 
                    if game_board[satr][sotoon] == "-" :
                        game_board[satr][sotoon] = "x"
                        show()
                        chek_plyer1()
                        break
                    elif "-" not in game_board[0]and "-" not in game_board[1] and "-" not in game_board[2]:
                        print("finish")
                        break
                    
        else:
            print("Enter a number bein 0 ta 2!")
            satr=int(input("Enter a number for satr:"))
            sotoon=int(input("Enter a number for sotoon:"))
            if 0 <= satr <3 and 0 <= sotoon < 3 : 
                if game_board[satr][sotoon] == "-" :
                    game_board[satr][sotoon] = "x"
                    show()
                    chek_plyer1()
                    break
                elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                    print("finish")
                    break
            else:
                print(" nobat to tamom shod")
                break



#plyer2
    print("plyer2")
    while True:
        satr=int(input("Enter a number for satr:"))
        sotoon=int(input("Enter a number for sotoon:"))
        if 0 <= satr <3 and 0 <= sotoon < 3 : 
            if game_board[satr][sotoon] == "-" :
                game_board[satr][sotoon] = "o"
                show()
                chek_plyer2()
                break
            elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                print("finish")
                break
            else:
                print("baiad ie khone dige antekhab koni in khone pore")
                satr=int(input("Enter a number for satr:"))
                sotoon=int(input("Enter a number for sotoon:"))
                if 0 <= satr <3 and 0 <= sotoon < 3 : 
                    if game_board[satr][sotoon] == "-" :
                        game_board[satr][sotoon] = "o"
                        show()
                        chek_plyer2()
                        break
                    elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                        print("finish")
                        break
                else:
                    print("Enter a number bein 0 ta 2")
                    satr=int(input("Enter a number for satr:"))
                    sotoon=int(input("Enter a number for sotoon:"))
                    if 0 <= satr <3 and 0 <= sotoon < 3 : 
                        if game_board[satr][sotoon] == "-" :
                            game_board[satr][sotoon] = "o"
                            show()
                            chek_plyer2()
                            break
                        elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                            print("finish")
                            break
        else:
            print("Enter a number bein 0 ta 2!")
            satr=int(input("Enter a number for satr:"))
            sotoon=int(input("Enter a number for sotoon:"))
            if 0 <= satr <3 and 0 <= sotoon < 3 : 
                if game_board[satr][sotoon] == "-" :
                    game_board[satr][sotoon] = "o"
                    show()
                    chek_plyer2()
                    break
                elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                    print("finish")
                    break
            else:
                print("nobat to tamom shod")
                break