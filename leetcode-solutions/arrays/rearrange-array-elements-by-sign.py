# Notes: https://leetcode.com/problems/rearrange-array-elements-by-sign/
# 
class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # The first positive integer of nums = res[0]
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        return [val for pair in zip(positives, negatives) for val in pair]

