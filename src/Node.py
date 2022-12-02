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
        self.__heuristic = None
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
            self.__children.append((new_node, play))

    def heuristic(self, next_node, move):
        """Heuristic of a play, the better the play the higher value."""
        board = next_node.__connect4.get_board()
        row = 0
        while row < 5 and board[row][move] == 0:
            row += 1
        player = board[row][move]
        assert player != 0
        finish_status = next_node.__connect4.finished()
        if finish_status != 0:
            if finish_status == player:
                return 1000
            else:
                return -1000
        return self.__check_contiguous(row, move, player, board)

    def __check_contiguous(self, row: int, column: int, player: int, board: list) -> int:
        """Aux private function to check for contiguous chips of the player."""
        contiguous = 0
        # down
        curr_row = row + 1
        while curr_row < 6 and board[curr_row][column] == player:
            contiguous += 1
            curr_row += 1

        # left
        curr_col = column - 1
        while curr_col > -1 and board[row][curr_col] == player:
            contiguous += 1
            curr_col -= 1

        # right
        curr_col = column + 1
        while curr_col < 7 and board[row][curr_col] == player:
            contiguous += 1
            curr_col += 1

        # up-right
        curr_row = row - 1
        curr_col = column + 1
        while curr_col < 7 and curr_row > -1 and board[curr_row][curr_col] == player:
            contiguous += 1
            curr_row -= 1
            curr_col += 1

        # up-left
        curr_row = row - 1
        curr_col = column - 1
        while curr_col > -1 and curr_row > -1 and board[curr_row][curr_col] == player:
            contiguous += 1
            curr_row -= 1
            curr_col -= 1

        # down-right
        curr_row = row + 1
        curr_col = column + 1
        while curr_col < 7 and curr_row < 6 and board[curr_row][curr_col] == player:
            contiguous += 1
            curr_row += 1
            curr_col += 1

        # down-left
        curr_row = row + 1
        curr_col = column - 1
        while curr_col > -1 and curr_row < 6 and board[curr_row][curr_col] == player:
            contiguous += 1
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