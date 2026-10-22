class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bool((n & (n-1)) == 0 and n)