from __future__ import annotations

class Board:
    

    def __init__(self, size: int = 0) -> Board:
        self.__size = size
        self.__board = self.__create_empty()


    def __create_empty(self) -> Board:
        board = []

        for r in range(self.__size):
            board.append([])
            for _ in range(self.__size):
                board[r].append(0)

        return board

    def __getitem__(self, key: int):
        if type(key) != int:
            raise KeyError
        return self.__board[key]

    def __len__(self):
        return len(self.__board)