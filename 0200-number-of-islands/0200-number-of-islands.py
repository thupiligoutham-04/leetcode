class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                return
            grid[x][y] = "0"
            dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            for r, c in dir:
                row = r + x
                col = c + y
                dfs(row, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans
