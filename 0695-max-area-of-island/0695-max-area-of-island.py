class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            curr_sum = 1
            grid[x][y] = 0
            dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for r, c in dir:
                row = r + x
                col = c + y
                curr_sum += dfs(row, col)
            return curr_sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = dfs(i, j)
                    max_area = max(max_area, curr)
        return max_area