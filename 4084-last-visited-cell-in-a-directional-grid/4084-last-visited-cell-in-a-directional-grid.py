class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        row = col = 0
        prow, pcol = 0, 0
        while row < m and col < n and row >= 0 and col >= 0 and not seen[row][col]:
            print('while')
            prow, pcol = row, col
            seen[row][col] = True
            if grid[row][col] == 'R':
                col += 1
            elif grid[row][col] == 'L':
                col -= 1
            elif grid[row][col] == 'U':
                row -= 1
            else:
                row += 1
        if row < m and col < n and row >= 0 and col >= 0 and (not seen[row][col]):
            return [row, col]
        else:
            return [prow, pcol]