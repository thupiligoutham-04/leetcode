class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)

        def isPal(l, r):
            while l > -1 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        x = y = 0
        first, last = 0, 0
        for i in range(n):
            if (x - y) // 2 > n - i:
                break
            x, y = isPal(i, i)
            if y - x > last - first:
                first, last = x, y
            x, y = isPal(i, i + 1)
            if y - x > last - first:
                first, last = x, y
        return s[first : last + 1]
