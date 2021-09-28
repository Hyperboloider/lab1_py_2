from board import Board

class BoardPrettifier:
    

    @staticmethod
    def prettify(board: Board):
        for r in range(len(board) - 1, -1, -1):
            crown_replaced = list(map(lambda x: '⊠' if x else '🗆', board[r]))
            for cell in crown_replaced:
                print(f" {cell} ", end="")
            print()
