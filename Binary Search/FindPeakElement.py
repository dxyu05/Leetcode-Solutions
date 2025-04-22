# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

class Solution:
    # i actually couldn't figure this out during my amazon interview, which sucks, since I realized this is actually 
    # quite a simple problem. Sucks a lot, and hopefully I can crack FAANG+ next year.

    # The key to solving this problem is realizing that you can return any peak
    # that means that if you continue to split the array in half (like binary search)
    # in the direction of the larger neighbor to the middle element, you will eventually find a peak
    # this is because if the middle element is not a peak, then one of its neighbors must be larger,
    # and if you continue to search in that direction, you will eventually find a peak.
    # this solution has a time complexity of O(log n) and a space complexity of O(1)

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            
            leftVal = 0
            rightVal = 0

            if middle == 0:
                leftVal = float('-inf')
            else: 
                leftVal = nums[middle - 1]
            
            if middle == len(nums) - 1:
                rightVal = float('-inf')
            else:
                rightVal = nums[middle + 1]

            if leftVal < nums[middle] and rightVal < nums[middle]:
                return middle
            elif nums[middle] < leftVal:
                right = middle - 1
            else:
                left = middle + 1

        return -1
    
    # solution 2
    # my original solution had a lot of unnecessary variables and checks do to the way I went about implementing the solution
    # there is a slighltly more clever way that can save us a few lines of code.

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left < right:
            middle = (right + left) // 2
            
            if nums[middle] < nums[middle + 1]:
                left = middle + 1
            else:
                right = middle
        # when the loop ends, left == right, and we can return either
            

        return nums[left]

        