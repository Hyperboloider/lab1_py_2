from typing import List, TypeVar
from node import EvaluatedNode, Node
from copy import deepcopy


class BoardGenerator:

    __T = TypeVar('__T', Node, EvaluatedNode)

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
