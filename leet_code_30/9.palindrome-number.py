#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x // div >= 10:
            div *= 10
        while x:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x%div) // 10
            div = div // 100
        return True
# @lc code=end

