class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        
        for i in range(0, len(nums)):
            temp = rob1
            rob1 = max(rob1, rob2 + nums[i])
            rob2 = temp
            
        return rob1
    
# leetcode 198 house robber
# basically we should always think of the subproblems we can solve at each step
# and we should probably start with a memoization table or array to store the results of the subproblems
# here we understand at each step we want the maximum amount of money we can rob up to that house
# then we realize we can either rob the current house and add it to the max
# amount robbed from two houses ago or we can skip the current house and take the max
# amount robbed from the previous house... this give us the recurrence relation
# memo[i] = max(memo[i-1], memo[i-2]) + nums[i])
# in recurrence form it would be in parentheses instead.
# upon furhter inspection we see that we only need the last two values of the memoization table
# to calculate the current value so we can just use two variables to store these values
# and update them as we iterate through the array...
# this gives us the optimal solution with O(n) time complexity and O(1) space complexity

        
            
            



        