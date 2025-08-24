class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        numZeros = 0
        maxTotal = 0
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1

            if numZeros > 1:
                maxTotal = max(maxTotal, r - l - 1)

                while numZeros > 1:
                    if nums[l] == 0:
                        numZeros -= 1
                    
                    l += 1

        return max(maxTotal, r - l)

# leetcode 1493 longest subarray of 1's after deleting one element
# another variable sized sliding window problem where we need to adjust the 
# size of the window whenever we have more than one zero in the window..
# this is because of the property of the problem where the array contains only 0s and 1s
# and we need to find the longest subarray of 1s after deleting one element..
# so we can keep one zero in the window...
# this solution is optimal with O(n) time complexity and O(1) space complexity