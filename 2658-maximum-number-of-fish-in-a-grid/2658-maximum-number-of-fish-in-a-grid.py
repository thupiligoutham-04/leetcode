class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        def dfs(x, y, fishes):
            fishes += grid[x][y]
            grid[x][y] = 0

            if x - 1 >= 0 and grid[x-1][y] > 0:
                fishes = dfs(x-1, y, fishes)
            if y - 1 >= 0 and grid[x][y-1] > 0:
                fishes = dfs(x, y-1, fishes)
            if y + 1 < n and grid[x][y+1] > 0:
                fishes = dfs(x, y+1, fishes)
            if x + 1 < m and grid[x+1][y] > 0:
                fishes = dfs(x+1, y, fishes)
            return fishes

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    curr = dfs(i, j, 0)
                    ans = max(ans, curr)
        return ans