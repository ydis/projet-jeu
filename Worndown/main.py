import game

game = True

#boucle pour le jeu
while game:

    #Menu
    print("                                            !!!WORNDOW!!!")
    print(                                              "Main Menu")
    print(                                               "")

    #Selection 
    print("1/ Start : ")
    print("2/ Show leaderboard")
    print("3/ Quit")

    menu_choice = input("menu_choice : ")

    if menu_choice == "1":
        game.start_game()# je dois le définir dans game.py
    elif menu_choice == "2":
        game.show_leaderboard()# à déf dans game.py
    elif menu_choice == "3":
        print("skill issue ?")
        game = False
    else:
        print("bruh try again it's just 3 choices")
    break       
