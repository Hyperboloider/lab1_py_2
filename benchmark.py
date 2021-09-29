from solver import IDSSolver, RBFSSolver, SearchResult, Solver
from inout import BoardPrettifier, Reader
from resources import Timer

class Benchmark:


    @classmethod
    def start(cls):
        filename = input('filename: ')
        board = Reader(filename).create_board()

        solve_choice = int(input('IDS - 0, RBFS - 1: '))
        solver = IDSSolver(board) if solve_choice == 0 else RBFSSolver(board)
        BoardPrettifier.prettify(board)

        print("method name:", solver.solve.__doc__)
        result = cls.__start_solving(solver)
        print(f'fail: {result.failure}, cutoff: {result.cutoff}, success: {result.success}')
        if result.success:
            BoardPrettifier.prettify(result.solution)

    
    @classmethod
    @Timer.timeit
    def __start_solving(cls, solver: Solver) -> SearchResult:
        return solver.solve()
