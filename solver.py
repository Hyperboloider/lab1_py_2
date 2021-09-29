from __future__ import annotations
from abc import abstractmethod
from typing import Tuple
from board import Board
from node import EvaluatedNode, Node
from validator import BoardValidator
from generator import BoardGenerator
import math


class SearchResult:


    def __init__(self, success = False, solution: Board = Board(), failure = False, cutoff = False):
        self.success = success
        self.failure = failure
        self.cutoff = cutoff
        self.solution = solution


class Solver:


    def __init__(self, board: Board) -> Solver:
        self._board = board
        self._root = Node(board, 0)

    @abstractmethod
    def solve(self):
        raise NotImplementedError

    @abstractmethod
    def _recursive_solve(self, node, limit):
        raise NotImplementedError


class IDSSolver(Solver):


    def solve(self):
        """Iterative Deepening Search"""

        for depth in range(len(self._board)):
            result = self._recursive_solve(self._root, depth)
            if not result.cutoff:
                return result
        
        return SearchResult(failure=True)

    def _recursive_solve(self, node: Node, limit: int) -> SearchResult:
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
                    result = self._recursive_solve(child, limit)

                    if result.cutoff:
                        cutoff_occured = True
                    else:
                        if result.success:
                            return result
        
        if cutoff_occured:
            return SearchResult(cutoff=True)
        else:
            return SearchResult(failure=True)


class RBFSSolver(Solver):


    def solve(self) -> SearchResult:
        """Recursive Best First Search"""

        result, _ = self._recursive_solve(self._root, math.inf)
        return result

    def _recursive_solve(self, node: EvaluatedNode, f_limit: int) -> Tuple(SearchResult, int):
        
        if BoardValidator(node.board).is_valid():
            return SearchResult(success=True, solution=node.board), None

        children = BoardGenerator().create_children(node)

        if not children:
            return SearchResult(failure=True), math.inf

        for child in children:
            child.evaluation = BoardValidator(child.board).evaluate()
        
        while True:
            children.sort(key = lambda x: x.evaluation)
            best = children[0]

            if best.evaluation > f_limit:
                return SearchResult(failure=True), best.evaluation

            alternative = children[1]
            result, best.evaluation = self._recursive_solve(best, min(f_limit, alternative.evaluation))
            if not result.failure:
                return result, None
            