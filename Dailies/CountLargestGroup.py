class Solution:
    # 4/23/2025 leetcode daily
    
    def countLargestGroup(self, n: int) -> int:
        # the problem is a bit confusing but we are supposed to just 
        # group the sum of the digits of the number from 1 to n
        # by sum of the digits, we mean for every number from 1 to n
        # the sum of its digits.. e.g 13 = 1 + 3 = 4.
        # 4 now has two numbers that sum to it, 4 and 13.
        
        hashmap = defaultdict(int)
        # instead of using a defaultdict there is a slight optimization using an array of size 36
        # because the constraints say i <= n <= 10^4 meaning the largest sum of digits is 36
        # because 9 + 9 + 9 + 9

        # loop from 1 to n
        for i in range(1, n + 1):
            theSum = 0

            #instead of doing this we could also convert to a string and use string manipulation
            while i > 0:
                theSum += i % 10
                i = i // 10

            hashmap[theSum] += 1

        
        maxOccurrences = 0
        maxCount = 0
        
        # putting it in the hashmap
        # we need to count the occurrences of the max occurrences lol
        for num in hashmap:
            if hashmap[num] > maxOccurrences:
                maxOccurrences = hashmap[num]
                maxCount = 1
            elif maxOccurrences == hashmap[num]:
                maxCount += 1

        return maxCount
            

        