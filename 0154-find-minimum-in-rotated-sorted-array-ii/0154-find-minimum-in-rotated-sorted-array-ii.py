class Solution:
    def findMin(self, nums: list[int]) -> int:
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]
        