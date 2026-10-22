class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        xor = 0
        xor_arr = []
        for num in arr:
            xor_arr.append(xor)
            xor ^= num
        xor_arr.append(xor)
        res = []
        for query in queries:
            ans = xor_arr[query[0]] ^ xor_arr[query[1] + 1]
            res.append(ans)
        return res
        