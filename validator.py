from board import Board


class BoardValidator:


    def __init__(self, board: Board):
        self.__board = board

    def is_valid(self) -> bool:
        for col in range(len(self.__board)):
            for row in range(len(self.__board)):
                if self.__board[row][col] == 1:
                    if not self.__quine_is_valid(row, col):
                        return False
        
        return True

    def __quine_is_valid(self, row: int, col: int) -> bool:
        #check horizonaly
        #main
        current_row = row + 1
        current_col = col - 1
        while current_row < len(self.__board) and current_col > -1:
            if self.__board[current_row][current_col] == 1: 
                return False
            current_col -= 1
            current_row += 1
        
        current_row = row - 1
        current_col = col + 1
        while current_row > -1 and current_col < len(self.__board):
            if self.__board[current_row][current_col] == 1: 
                return False
            current_col += 1
            current_row -= 1

        #additional
        current_row = row - 1
        current_col = col - 1
        while current_row > -1 and current_col > -1:
            if self.__board[current_row][current_col] == 1: 
                return False
            current_col -= 1
            current_row -= 1

        current_row = row + 1
        current_col = col + 1
        while current_row < len(self.__board) and current_col < len(self.__board):
            if self.__board[current_row][current_col] == 1: 
                return False
            current_col += 1
            current_row += 1

        #horizontally
        for c in range(len(self.__board)):
            if self.__board[row][c] == 1 and c != col:
                return False

        return True