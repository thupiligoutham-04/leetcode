class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        small = same = 0
        for num in nums:
            if num == target:
                same += 1
            elif num < target :
                small += 1

        return [i for i in range(small, small + same)]
        