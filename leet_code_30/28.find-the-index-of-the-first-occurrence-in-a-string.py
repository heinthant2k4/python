#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       #This want us to find needle in a haystack. Edge case is if needle is none, return 0. if needle not in haystack, return -1. if needle is in haystack, return index of first needle
       if not needle: return 0
       for i in range(len(haystack)-len(needle)+1):
           if haystack[i:i+len(needle)] == needle:
                return i
       return -1
    '''
    Tracing: haystack = "hello", needle = "ll"
    needle_len = 2
    haystack_len = 5
    for i in range(5-2+1): -> for i in range(4): i = 0,1,2,3
        i = 0: haystack[0:2] = "he" != "ll"
        i = 1: haystack[1:3] = "el" != "ll"
        i = 2: haystack[2:4] = "ll" == "ll" -> return 2
    Result: 2
    '''
# @lc code=end

