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
        #set the accumulator as 0
        total = 0
        #romans are read left to right, if smaller value is on left side of larger value, we subtract it from right value.
        #if larger value is on left side of smaller value, we add it to total.
        for a,b in zip(s,s[1:]):
        #zip is a function which takes two iterable and they are next to each other, if a is 0 then b is 1.
            if romans[a] < romans[b]:
                total -= romans[a]
            else:
                total += romans[a]
        #we need to add the last value since in zip last value is not included.
        total += romans[s[-1]]
        return total
# @lc code=end

