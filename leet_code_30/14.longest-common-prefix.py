#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #if str is empty -> return ""
        #we can set a prefix as the first character of the string
        #and iterate thourgh the rest of the strings
        #while the current string(iterable) is not starting with prefix. We use slicing to reduce prefix by one character s[:-1]. # and continue until we find the common prefix or prefix becomes empty, if it's not preix becomes empty, return ""
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# @lc code=end

