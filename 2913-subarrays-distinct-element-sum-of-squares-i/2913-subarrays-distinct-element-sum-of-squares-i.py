class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(0, n):
            distinct = set()
            for j in range(i, n):
                if nums[j] not in distinct:
                    distinct.add(nums[j])
                ans += len(distinct) ** 2
        return ans