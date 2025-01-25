# Notes: https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for x in nums:
            if x - 1 not in nums:  # Only start a sequence if x-1 isn't in the set
                length = 1
                while x + length in nums:
                    length += 1
                best = max(best, length)

        return best