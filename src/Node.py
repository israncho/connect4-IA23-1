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
            copy = Connect4.connect4(False, self.__connect4.get_board())
            copy.make_play(True if next_player == 1 else False, play)
            new_node = node(copy, next_player, self, self.__height + 1) 
            new_node.__heuristic = self.heuristic(self, play)
            self.__children.append((new_node, play))

    def heuristic(self, node, move):
        return None

    def get_children(self):
        """Function to get the children of this node."""
        return self.__children
    
    def get_height(self):
        return self.__height

b = Connect4.connect4()
n = node(b, 2)
queue = []
queue.append(n)
i = 0
count = 0
while i < 6:
    curr_node = queue.pop(0)
    print(count)
    count += 1
    curr_node.expand()
    for child in curr_node.get_children():
        queue.append(child[0])
    i = curr_node.get_height()