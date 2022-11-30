import Connect4


class node:
    """Class to model the nodes for the search model."""

    def __init__(self, connect4, current_player: int, parent= None, height: int = 0) -> None:
        """Constructor of a node"""
        assert type(connect4) == Connect4.connect4
        assert type(current_player) == int 
        assert height >= 0
        assert current_player == 1 or current_player == 2 
        self.__connect4 = Connect4.connect4(False, connect4.get_board())
        self.__children = []
        self.__current_player = current_player 
        self.__parent = parent 
        self.__heuristic = None
        self.__height = height 

    def __str__(self) -> str:
        return str(self.__connect4) + "\nplayer: "+ str(self.__current_player) + ", height: " + str(self.__height) + "\n\n"
    
    def expand(self) -> None:
        """Function to expand this node."""
        next_player = 1 if self.__current_player == 2 else 2
        for play in self.__connect4.possible_plays():
            copy = Connect4.connect4(self.__connect4.get_board())
            copy.make_play(True if next_player == 1 else False, play)
            new_node = node(copy, next_player, self, self.__height + 1) 
            new_node.heuristic = self.heuristic(self, play)
            self.__children.append(new_node)

    def heuristic(self, node, move):
        return None

    def get_children(self):
        """Function to get the children of this node."""
        return self.__children

b = Connect4.connect4()
n = node(b, 2)
print(n)
n.expand()
for node in n.get_children():
    print(node)