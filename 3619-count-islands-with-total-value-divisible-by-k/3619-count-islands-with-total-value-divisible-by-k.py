class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            curr_sum = grid[x][y] % k
            grid[x][y] = 0
            dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            for r, c in dir:
                row = x + r
                col = y + c
                curr_sum += dfs(row, col)
            return curr_sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    if dfs(i, j) % k == 0:
                        ans += 1
        return ans
