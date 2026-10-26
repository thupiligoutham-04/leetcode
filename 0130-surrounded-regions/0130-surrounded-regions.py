class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != "O":
                return
            board[x][y] = "#"
            dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for r, c in dir:
                row = r + x
                col = c + y
                dfs(row, col)

        for i in range(n):
            dfs(0, i)
        for i in range(1, m):
            dfs(i, n - 1)
        for i in range(n - 2, 0, -1):
            dfs(m - 1, i)
        for i in range(m - 1, 0, -1):
            dfs(i, 0)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
        