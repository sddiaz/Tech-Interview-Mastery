# Notes: https://leetcode.com/problems/sort-colors/description/
# 1. Sort like normal
# 2. Count frequencies
# 3. DNF Algorithm. 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1

        while (mid <= high):
            if (nums[mid] == 0):
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif (nums[mid] == 1):
                mid += 1
            elif (nums[mid] == 2):
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1