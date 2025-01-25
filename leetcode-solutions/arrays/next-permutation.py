# Notes: https://leetcode.com/problems/next-permutation/
# Find the first strictly decreasing subsequence. 
# Swap the root element (the element before that sequence) with the next smallest element in the decreasing sequence. 
# Reverse the sequence. 
class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a) - 1
        root = float('-inf')
        
        # Find the first decreasing pair from the right (i, i-1)
        for i in range(n, 0, -1):
            if (a[i] > a[i - 1]):
                # Find the next larger number than i -1, and swap it. 
                for j in range(n, i - 1, -1):
                    if (a[j] > a[i - 1]):
                        a[j], a[i - 1] = a[i - 1], a[j]
                        break 
                # Reverse from i to the end. 
                a[i:] = a[i:][::-1]
                return

        a.sort()