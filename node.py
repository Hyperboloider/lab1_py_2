from __future__ import annotations
from board import Board


class Node:


    def __init__(self, board: Board, depth: int):
        self.__board = board
        self.__depth = depth
    
    @property
    def board(self):
        return self.__board

    @property
    def depth(self):
        return self.__depth


class EvaluatedNode(Node):


    def __init__(self, board: Board, depth: int, evaluation: int):
        super.__init__(board, depth)
        self.evaluation = evaluation