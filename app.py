from solver import IDSSolver
from inout import BoardPrettifier
from board import Board


board = Board(8)
board[7][0] = 1 # 4 0
board[7][1] = 1 # 0 1
board[7][2] = 1 # 7 2
board[3][3] = 1 # 3 3
board[3][4] = 1 # 1 4
board[2][5] = 1 # 6 5
board[2][6] = 1 # 2 6
board[5][7] = 1 # 5 7

BoardPrettifier.prettify(board)
solver = IDSSolver(board, 5)
result = solver.iterative_deepening_search()
print(f'fail: {result.failure}, cutoff: {result.cutoff}, success: {result.success}')
if result.success:
    print('-'*10)
    BoardPrettifier.prettify(result.solution)