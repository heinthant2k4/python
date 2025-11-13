#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Thinking Process:
        let input x be 121.
        if -121 then its 121- -> false
        121 left and right must be equal to be a palindrome. For a 3 digit 121, 121 // 100 would be 1(from left), 121 % 10 would be 1(from right). We can pop middle element by 121 % 100 = 21 // 10 = 2. How do we find the divisor?
        for 12, divisor would be 10, for 121 divisor is 100. for n-digits, divisor is 10^n-1. let's start coding
        '''
        if x<0:
            return False
        div = 1
        #adding a power of 10 per iteration until x // div is a single digit
        while x // div >= 10:
            div *= 10
        while x:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div = div // 100 
            #removing by two digits since for 3 digit 10 is power 2, the result is a single digit. from 3 to 1(n -> n-2)+
            return True
# @lc code=end

