# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# ---------- Solution + Explanation -----------

# Intro

# While it may seem like a simple problem that can be solved with a greedy approach,
# it is actually a relatively tricky dynamic programming problem.
# The key (as always) for recursive/dynamic programming problems is to first determine
# the base case and to think about how we can break the problem down into smaller subproblems.
# For this problem we know we have to check if the string can be segmented into words
# and that means going through the string incrementing by one character at a time determing
# if the substring can be segmented into words. At first when I was solving this problem,
# I made the mistake of being too specific, deciding that at each character we could either 
# add it to the word or skip it. While this is true, it is not the best way to think about the problem.
# Instead, we should think about the problem in terms of the substring.
# We can use a recursive function to check if the substring can be segmented into words.
# We can also use memoization to store the results of the subproblems we have already solved.
# This will help us avoid recalculating the same subproblems over and over again.
# While can solve this problem using recursion and starting from the beginning of the string,
# the optimal solution is bottom-up dynamic programming, starting from the end of the string
# and looking back at the previous characters to determine if there is a valid segmentation.

# The gist of the solution is for each character in the string, we check if the substring
# from that character to the end of the string can be segmented into words.
# We do this by checking if the substring from that character to the end of the string is in the word dictionary
# If it is, we check if the substring from the next character to the end of the string can be segmented into words.
# If it is, we know at this character, we can segment the string into words.


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = [False] * (len(s) + 1)

        # the base case of course is that the empty string can be segmented
        # into words, so we set the last index of the memo array to True
        memo[-1] = True

        # we start from the end of the string and work our way back (because of the bottom-up approach)
        for i in range(len(s) - 1, -1, -1):
            # j is the end of the substring that we are checking
            # we check all the possible substrings, which are the substrings starting from i 
            # to the end of the string
            for j in range(i + 1, len(s) + 1):
                # if the substring from i to j is in the word dictionary
                # we need to check if the substring from j to the end of the string can be segmented into words
                # because that is the rest of the string that we need to be able to be segmented 
                # if it is, we can segment the string at this character and we will set the memo array to True
                # at this point, we can then break out of the loop
                # because we know we can segment the string at this character
                if s[i : j] in wordSet and memo[j]:
                    memo[i] = True
                    break

        # the first index of the memo array will tell us if we can segment the string
        # since we have computed the memo array from the end of the string to the beginning    
        # so this is our initial call
        return memo[0]
