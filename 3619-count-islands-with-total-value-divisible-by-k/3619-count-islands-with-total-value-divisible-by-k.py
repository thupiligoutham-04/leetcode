class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or (x, y) in visited:
                return 0
            curr_sum = grid[x][y] % k
            visited.add((x,y))
            dir = [(1,0), (0,1), (0, -1), (-1, 0)]
            for r, c in dir:
                row = x + r
                col = y + c
                if not (row < 0 or row >= m or col < 0 or col >= n or (row, col) in visited):
                    curr_sum += dfs(row, col)
                    curr_sum %= k
            return curr_sum
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in visited:
                    if dfs(i, j) % k == 0:
                        ans += 1
        
        return ans