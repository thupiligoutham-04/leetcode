class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(101)]
        for k, v in count.items():
            bucket[v].append(k)
        ans = []
        for i in range(101):
            for k in sorted(bucket[i], reverse = True):
                ans.extend([k] * i)
        return ans
        
        