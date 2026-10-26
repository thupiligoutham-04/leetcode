class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs(x, y, curr_sum):
            curr_sum += 1
            grid[x][y] = 0
            if x + 1 < m and grid[x + 1][y] == 1:
                curr_sum = dfs(x + 1, y, curr_sum)
            if x - 1 >= 0 and grid[x - 1][y] == 1:
                curr_sum = dfs(x - 1, y, curr_sum)
            if y + 1 < n and grid[x][y + 1] == 1:
                curr_sum = dfs(x, y + 1, curr_sum)
            if y - 1 >= 0 and grid[x][y - 1] == 1:
                curr_sum = dfs(x, y - 1, curr_sum)
            return curr_sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = dfs(i, j, 0)
                    max_area = max(max_area, curr)
        return max_area
