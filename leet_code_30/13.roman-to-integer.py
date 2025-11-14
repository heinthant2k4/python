#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        #create a dict
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for a, b in zip(s,s[1:]):
            if romans[a] < romans[b]:
                result -= romans[a]
            else:
                result += romans[a]
        result += romans[s[-1]]
        return result
# @lc code=end

