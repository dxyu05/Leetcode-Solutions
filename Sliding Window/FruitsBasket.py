class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap = {}
        maxTotal = 0
        l = 0
        
        for r in range(0, len(fruits)):
            if fruits[r] not in hashmap:
                hashmap[fruits[r]] = 1
            else:
                hashmap[fruits[r]] += 1

            while len(hashmap) > 2:
                if hashmap[fruits[l]] > 1:
                    hashmap[fruits[l]] -= 1
                else:
                    del hashmap[fruits[l]]

                l += 1

            maxTotal = max(maxTotal, r - l + 1)

        return maxTotal


# leetcode 904 fruit into basket
# the main pattern here is to continuously adjust the left size of the window whenever
# we have more than 2 types of fruits in the basket. Time complexity O(n) Memory complexity O(1)
# a hashmap comes in handy here and maintaining the count of each fruit type is actually very important
# this makes my original idea of just using variables to track the counts way too complicated
# moral of the story don't try to be fancy at first just try to find a good solution