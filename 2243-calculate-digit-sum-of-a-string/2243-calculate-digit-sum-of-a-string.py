class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def getSum(x):
            ans = str(sum(map(int, x)))
            return ans
            
        while len(s) > k:
            res = []
            for i in range(0, len(s), k):
                res.append(getSum(s[i:i + k]))
            s = "".join(res)
        return s