from board import Board
from generator import BoardGenerator
from solver import IDSSolver, Parameters, RBFSSolver, SearchResult, Solver
from inout import BoardPrettifier, Reader
from resources import Timer

class Benchmark:


    @classmethod
    def start(cls, board: Board, solve_choice: int):
        """"solve chiice(IDS: 0; RBFS: 1)"""
        parameters = Parameters()
        solver = IDSSolver(board, parameters) if solve_choice == 0 else RBFSSolver(board, parameters)
        BoardPrettifier.prettify(board)
        
        print('method name:', solver.solve.__doc__)
        result = cls.__start_solving(solver)
        result.describe()
        parameters.describe()

    @classmethod
    def start_manual(cls):
        filename = input('filename: ')
        board = Reader(filename).create_board()
        solve_choice = int(input('IDS - 0, RBFS - 1: '))
        cls.start(board, solve_choice)

    @classmethod
    def start_automated(cls, numbre_of_tests: int = 20):
        for iteration in range(numbre_of_tests):
            print(iteration)
            board = BoardGenerator.create_pseudorandom_board(BoardGenerator.SOLVED_BOARD)
            solve_choice = 0
            print('='*25)
            cls.start(board, solve_choice)
            solve_choice = 1
            print('='*25)
            cls.start(board, solve_choice)
            print('='*25)

    @classmethod
    @Timer.timeit
    def __start_solving(cls, solver: Solver) -> SearchResult:
        return solver.solve()
