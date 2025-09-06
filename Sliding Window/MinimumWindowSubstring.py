class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap = defaultdict(int)
        tmap = defaultdict(int)

        for c in t:
            tmap[c] += 1

        minSubstring = ""
        minLength = float('inf')
        l = 0
        difference = len(tmap)

        for r in range(len(s)):
            if s[r] in tmap:
                smap[s[r]] += 1

                if smap[s[r]] == tmap[s[r]]:
                    difference -= 1

            if difference == 0:             
                while difference == 0:
                    if s[l] in tmap:
                        smap[s[l]] -= 1

                        if smap[s[l]] < tmap[s[l]]:
                            difference += 1
                        
                    l += 1
                
                if r - l + 1 < minLength:
                    minSubstring = s[l - 1:r + 1]
                    minLength = len(minSubstring)

        return minSubstring


# the key here is using two hashmaps and having a clever way of avoiding
# O(n) traversal of the hashmap to check if we have a valid window
# we can do this by keeping track of the number of characters that are
# different between the two hashmaps...
# so making sure we have the same characters in the current window as in t 
# but also the same number of occurrences of each character
# we actually only need to meet a minimum number of occurrences for each character
# and we can use if statements to make sure we don't exceed the number of occurrences
# we can then make the window smaller by moving the left pointer until the number of occurences
# falls below the required number for any character in t and keep track of the minimum length substring
# this solution is optimal with O(n) time complexity and O(m) space complexity where m is the length of t
# leetcode 76 minimum window substring





        
        