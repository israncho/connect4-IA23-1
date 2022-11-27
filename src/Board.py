import copy


class board:
    """Class to model a connect4 board."""

    def __init__(self):
        """Constructor of the board."""
        self.__matrix = []
        for i in range(6):
            self.__matrix.append([0, 0, 0, 0, 0, 0, 0])

    def __str__(self) -> str:
        """str function of a connect 4 board."""
        string = ""
        for row in self.__matrix:
            string += " | "
            for cell in row:
                string += str(cell) + " "
            string += "\n"
        string += " | _____________\n"
        string += "   0 1 2 3 4 5 6"
        return string

    def __eq__(self, board) -> bool:
        """Equals function to compare two boards."""
        if type(self) != type(board):
            return False
        for i in range(6):
            for j in range(7):
                if self.__matrix[i][j] != board.__matrix[i][j]:
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
        while self.__matrix[row][column] != 0:
            row -= 1
            if row < 0:
                return True
        if player_one:
            self.__matrix[row][column] = 1
        else:
            self.__matrix[row][column] = 2
        return False

    def get_board(self) -> list:
        """Returns a copy of the board"""
        return copy.deepcopy(self.__matrix)

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
                    return current
        # check for win by a vertical play
        for column in range(7):
            (current, contiguous) = (0, 0)
            for row in range(6):
                (current, contiguous) = self.__check_contiguous(
                    row, column, current, contiguous)
                if contiguous == 4:
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
                    return current
                row += 1
                column += 1
        return 0

    def __check_contiguous(self, row, column, current, contiguous) -> tuple:
        """Auxiliary function to check winning plays."""
        cell = self.__matrix[row][column]
        if cell == 0:
            return (0, 0)
        if cell != current:
            return (cell, 1)
        return (current, contiguous + 1)


b = board()
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
