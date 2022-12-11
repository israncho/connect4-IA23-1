import Connect4
import Node


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
curr_node = Node.node(game, 2)
curr_node.expand()

player1 = True
while game.finished() == 0 and game.possible_plays() != []:
    print(game)
    play = None
    if player1:
        print("player1 make a play: ", end="")
        play = user_input() 
    else:
        # children is a list of tuples, (child, play)
        children = curr_node.get_children()
        (curr_best_heuristic, curr_best_play) = (children[0][0].get_heuristic(), children[0][1])
        for (child, curr_play) in children:
            if child.get_heuristic() > curr_best_heuristic:
                curr_best_heuristic = child.get_heuristic()
                curr_best_play = curr_play
                curr_node = child
        curr_node.height_4_tree()
        play = curr_best_play


    if game.make_play(player1, play):
        print(" Invalid play!!!!!!!!\n")
        continue
    if player1:
        for (child, posible_play) in curr_node.get_children():
            if play == posible_play:
                curr_node = child 
        curr_node.height_4_tree()
        player1 = False
    else:
        player1 = True
    print()

print(game)
if game.winner == 0:
    print("There was a tie.")
else:    
    print("The winner is player " + str(game.winner))
