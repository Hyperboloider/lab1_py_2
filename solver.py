from __future__ import annotations
from board import Board
from node import Node
from validator import BoardValidator
from generator import BoardGenerator


class SearchResult:


    def __init__(self, success = False, solution: Board = Board(), failure = False, cutoff = False):
        self.success = success
        self.failure = failure
        self.cutoff = cutoff
        self.solution = solution


class IDSSolver:


    def __init__(self, board: Board, max_depth: int) -> IDSSolver:
        self.__board = board
        self.__root = Node(board, 0, [])

    def iterative_deepening_search(self):
        for depth in range(len(self.__board)):
            result = self.__recursive_depth_limit_search(self.__root, depth)
            if not result.cutoff:
                return result
        
        return SearchResult(failure=True)

    def __recursive_depth_limit_search(self, node: Node, limit: int) -> SearchResult:
        cutoff_occured = False
        validator = BoardValidator(node.board)
        if validator.is_valid():
            return SearchResult(success=True, solution=node.board)
        else:
            if node.depth == limit:
                return SearchResult(cutoff=True)
            else:
                children = BoardGenerator.create_children(node)
                for child in children:
                    result = self.__recursive_depth_limit_search(child, limit)

                    if result.cutoff:
                        cutoff_occured = True
                    else:
                        if result.success:
                            return result
        
        if cutoff_occured:
            return SearchResult(cutoff=True)
        else:
            return SearchResult(failure=True)