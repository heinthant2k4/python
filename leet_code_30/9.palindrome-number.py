#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        div = 1
        #121 // 1 = 121 >= 10 (1st)
        #121 // 10 = 12 >= 10 (2nd)
        #12 // 100 = 1 < 10 (end) divisor is 100 
        while x // div >= 10:
            div *= 10
        while x:
            left = x // div #get leftmost digit(121 // 100 = 1)
            right  = x % 10 #get rightmost digit(121 % 10 = 1)
            if left != right: return False
            #remove l and r digits
            x = (x % div) // 10 
            #121 % 100 = 21 // 10 = 2(mid digit)
            div = div // 100 #reduce divisor by 2 digits (because we removed 2 digits)
        return True
# @lc code=end

