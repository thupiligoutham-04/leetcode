class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        xor = 0
        xor_arr = [0]
        for num in arr:
            xor ^= num
            xor_arr.append(xor)
        res = []
        for left, right in queries:
            res.append(xor_arr[left] ^ xor_arr[right + 1])
        return res
