import Connect4


def user_input() -> int:
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
while game.finished() == 0:
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
print("El ganador es el jugador " + str(game.winner))
