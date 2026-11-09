class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        table = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for row in range(n):
                        if j != row and grid[i][row]:
                            ans += 1
                            break
                    else:
                        for col in range(m):
                            if i != col and grid[col][j]:
                                ans += 1
                                break
        return ans