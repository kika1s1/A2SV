from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return

            board[i][j] = 'B'  # Mark the cell as 'B' to indicate it's not surrounded

            # Recursively check neighboring cells
            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i, j + 1)  # Right

        if not board:
            return

        rows, cols = len(board), len(board[0])

        # Check the boundaries for the first and last columns
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        # Check the boundaries for the first and last rows
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        # Flip 'O' cells to 'X' and 'B' cells to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'