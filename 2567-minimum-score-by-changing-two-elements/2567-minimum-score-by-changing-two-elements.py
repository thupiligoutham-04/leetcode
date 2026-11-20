class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) < 4: return 0
        # nums.sort()
        # return min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])
        low1 = low2 = low3 = float("inf")
        high1 = high2 = high3 = float("-inf")
        for num in nums:
            if num < low1:
                low1, low2, low3 = num, low1, low2
            elif num < low2:
                low2, low3 = num, low2
            elif num < low3:
                low3 = num

            if num > high1:
                high1, high2, high3 = num, high1, high2
            elif num > high2:
                high2, high3 = num, high2
            elif num > high3:
                high3 = num
            
        return min(high3 - low1, high2 - low2, high1 - low3)