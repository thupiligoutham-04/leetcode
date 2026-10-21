class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        print(-4 % 3)
        m, n = len(mat), len(mat[0])
        k = k % n
        if k == 0:
            return True
        for i in range(m):
            for j in range(n):
                if i % 2:
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
                else:
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
        return True
        