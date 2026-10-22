class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        lsum, rprod = sum(nums), 1
        ans = -1
        for i in reversed(range(len(nums))):
            lsum -= nums[i]
            if lsum == rprod:
                ans = i
            if lsum < rprod:
                break

            rprod *= nums[i]

        return ans
