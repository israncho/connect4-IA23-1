import Connect4


def user_input() -> int:
    """Function to get a valid play from the user."""
    not_finished = True
    while not_finished:
        usr_input = input()
        usr_int = -1
        try:
            usr_int = int(usr_input)
        except:
            print("Must enter a number!!\n\nTry again: ",end="")
            continue
        if usr_int > 6 or usr_int < 0:
            print("Invalid number!!\n\nTry again: ",end="")
            continue
        not_finished = False 
    return usr_int 

game = Connect4.connect4()

player1 = True
while game.finished() == 0 and game.possible_plays() != []:
    print(game)
    print("player", end="")
    if player1:
        print("1", end="")
    else:
        print("2", end="")
    print(" make a play: ", end="")
    play = user_input() 
    game.make_play(player1, int(play))
    if player1:
        player1 = False
    else:
        player1 = True
    print()

print(game)
print("The winner is player " + str(game.winner))
