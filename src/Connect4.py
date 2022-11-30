import copy


class connect4:
    """Class to model a connect4 board."""

    def __init__(self, new_game: bool = True, game_board: list = []):
        """Constructor of the board."""
        self.winner = 0
        self.__board = []
        if not new_game:
            assert len(game_board) == 6
            for row in game_board:
                assert len(row) == 7
                for cell in row:
                    assert type(cell) == int and cell > -1 and cell < 3
            self.__board = game_board
            return
        for i in range(6):
            self.__board.append([0, 0, 0, 0, 0, 0, 0])

    def __str__(self) -> str:
        """str function of a connect 4 board."""
        string = ""
        n = 0
        string += "    0 1 2 3 4 5 6\n"
        string += "    _____________\n"
        for row in self.__board:
            string += str(n) + " | "
            n += 1
            for cell in row:
                string += str(cell) + " "
            string += "\n"
        return string

    def __eq__(self, board) -> bool:
        """Equals function to compare two boards."""
        if type(self) != type(board):
            return False
        for i in range(6):
            for j in range(7):
                if self.__board[i][j] != board.__board[i][j]:
                    return False
        return True

    def make_play(self, player_one: bool, column: int) -> bool:
        """Function to make a play on the board.
        Returns True if the play could not be made."""
        if type(player_one) != bool or type(column) != int:
            raise Exception("Wrong argument.")
        if 0 > column or column > 6:
            raise Exception("Wrong column.")
        row = 5
        while self.__board[row][column] != 0:
            row -= 1
            if row < 0:
                return True
        if player_one:
            self.__board[row][column] = 1
        else:
            self.__board[row][column] = 2
        return False

    def get_board(self) -> list:
        """Returns a copy of the board"""
        return copy.deepcopy(self.__board)

    def finished(self) -> int:
        """Checks the board for a winner. If there is a winnner, 
        returns the player number of the winner, otherwise returns 0."""
        (current, contiguous) = (0, 0)
        # check for win by a horizontal play
        for row in range(6):
            (current, contiguous) = (0, 0)
            for column in range(7):
                (current, contiguous) = self.__check_contiguous(
                    row, column, current, contiguous)
                if contiguous == 4:
                    self.winner = current
                    return current
        # check for win by a vertical play
        for column in range(7):
            (current, contiguous) = (0, 0)
            for row in range(6):
                (current, contiguous) = self.__check_contiguous(
                    row, column, current, contiguous)
                if contiguous == 4:
                    self.winner = current
                    return current
        # check for win by a diagonal play (/)
        l = [(0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6)]
        for i in l:
            (row, column) = i
            (current, contiguous) = (0, 0)
            while row < 6 and column > -1:
                (current, contiguous) = self.__check_contiguous(
                    row, column, current, contiguous)
                if contiguous == 4:
                    self.winner = current
                    return current
                row += 1
                column -= 1
        # check for win by a diagonal play (/)
        l = [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3)]
        for i in l:
            (row, column) = i
            (current, contiguous) = (0, 0)
            while row < 6 and column < 7:
                (current, contiguous) = self.__check_contiguous(
                    row, column, current, contiguous)
                if contiguous == 4:
                    self.winner = current
                    return current
                row += 1
                column += 1
        return 0

    def __check_contiguous(self, row, column, current, contiguous) -> tuple:
        """Auxiliary function to check winning plays."""
        cell = self.__board[row][column]
        if cell == 0:
            return (0, 0)
        if cell != current:
            return (cell, 1)
        return (current, contiguous + 1)


"""
b = connect4()
b.make_play(True, 0)
b.make_play(True, 0)
b.make_play(True, 0)
b.make_play(True, 1)
b.make_play(True, 1)
b.make_play(True, 2)
b.make_play(False, 0)
b.make_play(False, 1)
b.make_play(False, 2)
b.make_play(True, 3)
print(b)
print("finished: " + str(b.finished()))
b = connect4()
print(b)
c = connect4(False, b.get_board())
print(c)
c.make_play(True, 0)
c.make_play(True, 0)
c.make_play(True, 0)
c.make_play(True, 0)
print(c)
print(b)
"""