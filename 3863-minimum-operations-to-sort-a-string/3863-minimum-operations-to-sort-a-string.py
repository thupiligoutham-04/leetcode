class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        isSorted = True
        for i in range(n-1):
            if s[i] > s[i+1]:
                isSorted = False
                break
        
        if isSorted: return 0
        if n == 2: return -1
        mx, mn = 'a', 'z'
        for ch in s:
            if ch > mx: mx = ch
            if ch < mn: mn = ch
        mnc = mxc = 0
        for ch in s:
            if ch == mn: mnc += 1
            if ch == mx: mxc += 1
        adv = mxc > 1 or mnc > 1
        if s[0] == mn or s[n-1] == mx:
            return 1
        elif s[0] == mx and s[n-1] == mn and not adv:
            return 3
        else :
            return 2
