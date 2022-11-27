import Connect4

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
    play = input()
    game.make_play(player1, int(play))
    if player1:
        player1 = False
    else:
        player1 = True
    print()

print(game)
print("El ganador es el jugador " + str(game.winner))
