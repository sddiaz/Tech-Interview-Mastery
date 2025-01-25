# Notes: https://leetcode.com/problems/maximum-subarray/
# Kadane's Algorithm, keep track of max so far + total sum. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            maxSoFar = max(maxSoFar + nums[i], nums[i])
            res = max(res, maxSoFar)
        return res