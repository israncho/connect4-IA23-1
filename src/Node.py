import Connect4


class node:
    """Class to model the nodes for the search model."""

    def __init__(self, connect4, current_player: int, parent=None, height: int = 0) -> None:
        """Constructor of a node"""
        assert type(connect4) == Connect4.connect4
        assert type(current_player) == int
        assert height >= 0
        assert current_player == 1 or current_player == 2
        self.__connect4 = Connect4.connect4(False, connect4.get_board())
        self.__children = []
        self.__current_player = current_player
        self.__parent = parent
        self.__heuristic = 0 
        self.__height = height

    def __str__(self) -> str:
        return str(self.__connect4) + "\nplayer: " + str(self.__current_player) + ", height: " + str(self.__height) + ", heuristic: " + str(self.__heuristic) + "\n\n"

    def expand(self) -> None:
        """Function to expand this node."""
        next_player = 1 if self.__current_player == 2 else 2
        for play in self.__connect4.possible_plays():
            copy = Connect4.connect4(False, self.__connect4.get_board())
            copy.make_play(True if next_player == 1 else False, play)
            new_node = node(copy, next_player, self, self.__height + 1)
            new_node.__heuristic = self.heuristic(new_node, play)
            self.__heuristic -= new_node.__heuristic * .14
            self.__update_heuristic(4)
            self.__children.append((new_node, play))
    
    def __update_heuristic(self, up_levels) -> None:
        """Aux function to update the heuristic of ancestor nodes."""
        if up_levels <= 0 or self.__parent == None:
            return
        self.__parent.__heuristic -= self.__heuristic * .14
        self.__parent.__update_heuristic(up_levels - 1)
        

    def heuristic(self, next_node, move):
        """Heuristic of a play, the better the play the higher value."""
        board = next_node.__connect4.get_board()
        row = 0
        while row < 5 and board[row][move] == 0:
            row += 1
        player = board[row][move]
        assert player != 0
        if next_node.__connect4.finished() == player:
            return 1000000
        return self.__check_contiguous(row, move, player, board)

    def __check_contiguous(self, row: int, column: int, player: int, board: list) -> int:
        """Aux private function to check for contiguous chips of the player."""
        contiguous = 0
        # down
        mult = 1
        curr_row = row + 1
        while curr_row < 6 and board[curr_row][column] == player:
            contiguous += mult
            mult += 4
            curr_row += 1

        # left
        mult = 1
        curr_col = column - 1
        while curr_col > -1 and board[row][curr_col] == player:
            contiguous += mult
            mult += 4
            curr_col -= 1

        # right
        mult = 1
        curr_col = column + 1
        while curr_col < 7 and board[row][curr_col] == player:
            contiguous += mult
            mult += 4
            curr_col += 1

        # up-right
        mult = 1
        curr_row = row - 1
        curr_col = column + 1
        while curr_col < 7 and curr_row > -1 and board[curr_row][curr_col] == player:
            contiguous += mult
            mult += 4
            curr_row -= 1
            curr_col += 1

        # up-left
        mult = 1
        curr_row = row - 1
        curr_col = column - 1
        while curr_col > -1 and curr_row > -1 and board[curr_row][curr_col] == player:
            contiguous += mult
            mult += 4
            curr_row -= 1
            curr_col -= 1

        # down-right
        mult = 1
        curr_row = row + 1
        curr_col = column + 1
        while curr_col < 7 and curr_row < 6 and board[curr_row][curr_col] == player:
            contiguous += mult
            mult += 4
            curr_row += 1
            curr_col += 1

        # down-left
        mult = 1
        curr_row = row + 1
        curr_col = column - 1
        while curr_col > -1 and curr_row < 6 and board[curr_row][curr_col] == player:
            contiguous += mult
            mult += 4
            curr_row += 1
            curr_col -= 1
        return contiguous

    def get_children(self):
        """Function to get the children of this node."""
        return self.__children

    def get_height(self):
        """Function to get the height of this node."""
        return self.__height


"""
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
"""
"""
b = Connect4.connect4()

b.make_play(False, 1)
b.make_play(True, 1)
b.make_play(False, 1)
b.make_play(True, 1)
b.make_play(True, 1)

n = node(b, 2)
n.expand()

n = node(b, 2)
n.expand()
print(n.get_children()[1][0])
print(n.heuristic(n.get_children()[1][0], n.get_children()[1][1]))
"""

b = Connect4.connect4()
n = node(b, 2)
n.expand()
for (child, play) in n.get_children():
    child.expand()
    for (c,p) in child.get_children():
        c.expand()

print(n)
for (child, play) in n.get_children():
    print("--------------------------------------------------------------------------------")
    print(child)
    for (c, p) in child.get_children():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(c)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        for (cc, pp) in c.get_children():
            print(cc)
    print("--------------------------------------------------------------------------------")
