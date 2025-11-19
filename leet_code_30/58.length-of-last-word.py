#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #A very easy problem, solution is in the question itself, word is a maximal substring without whitespace. We just split the array of characters which is list and then return the last value
        word = s.split()
        if not word:
            return 0
        return len(word[-1])
# @lc code=end

