class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        min = fresh = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for dx, dy in dir:
                    x, y = i + dx, j + dy
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        queue.append((x, y))
            min += 1

        return -1 if fresh else min