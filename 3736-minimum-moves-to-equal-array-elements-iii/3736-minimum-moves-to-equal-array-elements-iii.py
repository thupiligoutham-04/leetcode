class Solution:
    def minMoves(self, nums: List[int]) -> int:
        high, ans, n = nums[0], 0, len(nums)
        for i in range(1, n):
            if nums[i] < high:
                ans += high - nums[i]
            elif nums[i] > high:
                ans += i * (-high + nums[i])
                high = nums[i]
        return ans