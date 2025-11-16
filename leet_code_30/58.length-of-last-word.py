#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #This problem wants us to find the length of the last word in a string. We can do this by splitting the string by spaces and returning the length of the last element in the resulting list. 
        words = s.split()
        if not words:
            return 0
        return len(words[-1])
# @lc code=end

