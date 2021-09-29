from board import Board

class BoardPrettifier:
    

    @staticmethod
    def prettify(board: Board):
        for r in range(len(board) - 1, -1, -1):
            crown_replaced = list(map(lambda x: '⊠' if x else '🗆', board[r]))
            for cell in crown_replaced:
                print(f" {cell} ", end="")
            print()


class Reader:


    def __init__(self, filename: str):
        self.__filename = filename

    def create_board(self) -> Board:
        with open(self.__filename) as file:
            dimension = int(file.readline())
            queens = [int(x) for x in file.readline().split()]

            board = Board(dimension)
            for column, row in enumerate(queens):
                board[row][column] = 1

        return board