from board import Board
from typing import List, TypeVar
from node import EvaluatedNode, Node
from random import randint
from copy import deepcopy


class BoardGenerator:

    __T = TypeVar('__T', Node, EvaluatedNode)
    SOLVED_BOARD = [4, 0, 7, 3, 1, 6, 2, 5]

    @staticmethod
    def create_pseudorandom_board(solved_queen_position: List[int]) -> Board:
        board = Board(len(solved_queen_position))
        for column, row in enumerate(solved_queen_position):
            if randint(0, 1) == 0:
                board[row][column] = 1
            else:
                r = randint(0, 7)
                board[r][column] = 1
        
        return board

    @staticmethod
    def create_children(node: __T) ->List[__T]:
        children = []

        for c in range(len(node.board)):

            currnt_queen_row = 0
            for r in range(len(node.board)):
                if node.board[r][c] == 1:
                    currnt_queen_row = r
                    break

            for r in range(len(node.board)):
                if r == currnt_queen_row: 
                    continue

                new_board = deepcopy(node.board)
                new_board[currnt_queen_row][c] = 0
                new_board[r][c] = 1
                new_node = Node(new_board, node.depth + 1) if type(node) == Node else EvaluatedNode(new_board, node.depth, 0)
                children.append(new_node)

        return children
