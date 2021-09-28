from typing import List
from node import Node
from copy import deepcopy


class BoardGenerator:


    @staticmethod
    def create_children(node: Node) ->List[Node]:
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
                new_node = Node(new_board, node.depth + 1, [])
                children.append(new_node)

        return children
