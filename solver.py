from __future__ import annotations
from abc import abstractmethod
from inout import BoardPrettifier
from typing import Tuple
from board import Board
from node import EvaluatedNode, Node
from validator import BoardValidator
from generator import BoardGenerator
import math


class SearchResult:


    def __init__(self, success = False, solution: Board = Board(size=0), failure = False, cutoff = False):
        self.success = success
        self.failure = failure
        self.cutoff = cutoff
        self.solution = solution

    def describe(self):
        print(f'fail: {self.failure}, cutoff: {self.cutoff}, success: {self.success}')
        if self.success:
            BoardPrettifier.prettify(self.solution)
        

class Parameters:


    def __init__(self):
        self.iterations = 0
        self.states = 0
        self.memory_states = 0
        self.cutoffs = 0

    def describe(self):
        print(f'iterations: {self.iterations}, states: {self.states}, memory states: {self.memory_states}, cutoffs: {self.cutoffs}')


class Solver:


    def __init__(self, board: Board, parameters: Parameters) -> Solver:
        self._board = board
        self._root = Node(board, 0)
        self.parameters = parameters

    @abstractmethod
    def solve(self):
        raise NotImplementedError

    @abstractmethod
    def _recursive_solve(self, node, limit):
        raise NotImplementedError


class IDSSolver(Solver):


    def solve(self):
        """Iterative Deepening Search"""
        self.parameters.memory_states += 1
        self.parameters.states += 1
        for depth in range(len(self._board)):
            result = self._recursive_solve(self._root, depth)
            if not result.cutoff:
                return result
        
        return SearchResult(failure=True)

    def _recursive_solve(self, node: Node, limit: int) -> SearchResult:
        self.parameters.iterations += 1
        cutoff_occured = False
        validator = BoardValidator(node.board)
        if validator.is_valid():
            return SearchResult(success=True, solution=node.board)
        else:
            if node.depth == limit:
                self.parameters.cutoffs += 1
                return SearchResult(cutoff=True)
            else:
                children = BoardGenerator.create_children(node)
                self.parameters.states += len(children)
                self.parameters.memory_states += len(children)
                for child in children:
                    result = self._recursive_solve(child, limit)

                    if result.cutoff:
                        cutoff_occured = True
                    else:
                        if result.success:
                            return result

            self.parameters.memory_states -= len(children)

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
        self.parameters.iterations += 1
        if BoardValidator(node.board).is_valid():
            return SearchResult(success=True, solution=node.board), None

        children = BoardGenerator().create_children(node)

        if not children or node.depth > len(node.board):
            self.parameters.cutoffs += 1
            return SearchResult(failure=True), math.inf

        for child in children:
            child.evaluation = BoardValidator(child.board).evaluate()
        self.parameters.states += len(children)
        self.parameters.memory_states += len(children)

        while True:
            children.sort(key = lambda x: x.evaluation)
            best = children[0]

            if best.evaluation > f_limit:
                self.parameters.memory_states -= len(children)
                return SearchResult(failure=True), best.evaluation

            alternative = children[1]
            result, best.evaluation = self._recursive_solve(best, min(f_limit, alternative.evaluation))
            if not result.failure:
                return result, None
            