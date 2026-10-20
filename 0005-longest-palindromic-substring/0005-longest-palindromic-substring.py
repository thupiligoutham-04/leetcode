class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)

        def isPal(l, r):
            while l > -1 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            print(s[l+1:r])
            return s[l+1:r]

        maxPal = ''
        for i in range(n):
            odd = isPal(i, i)
            even = isPal(i, i + 1)
            maxPal = odd if len(odd) > len(even) else even
            if len(ans) < len(maxPal):
                ans = maxPal
        return ans
