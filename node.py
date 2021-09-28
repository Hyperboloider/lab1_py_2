from __future__ import annotations
from board import Board
from typing import List


class Node:


    def __init__(self, board: Board, depth: int, children: List[Node]):
        self.__board = board
        self.__depth = depth
        self.children = children
    
    @property
    def board(self):
        return self.__board

    @property
    def depth(self):
        return self.__depth
