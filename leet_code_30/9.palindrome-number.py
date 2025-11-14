#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #we have two methods to do this, I will comment out the string method
        #first we check if x is <0 since -121 != 121-
        if x<0:
            return False
        #we set divisor to 1 first
        div = 1
        while x // div >= 10: #we find the divisor
            div *= 10
        while x: #until x !< 0: we take left by dividing with divisor and right by modulating with 10. if left and right are not equal then false. we take the middle by modulating with divisor and dividing with 10, then reduce div by 2 digits
            left = x // div
            right = x % 10
            if left != right: return False
            x = (x % div) // 10
            div = div / 100
        return True
    '''
    Tracing: input: (a) 121 and (b) 1221
    for (a): div = 1, x = 121
    since x>121, pass
    121 // 1 = 121 >= 10 -> 1(div)*10 = 10
    121 // 10 = 12 >= 10 ->10(div)*10=100
    121/ 100 = 1 !>= 10 -> div is 100
    while x is not less than zero:
    we take left by dividing 121 with 100.
    1_21 = 121 // 100 = 1(from left)
    right by moduolo 10
    12_1 % 10 = 1
    if left != right: false, since 1=1: true
    taking middle digit = (1_2_1%100)->21//10->2
    reducing divisor by two digits.
    100 / 100 = 1
    at second iteration: x is now 2.
    Thus while x:
    left = 2 // 1 = 2
    right = 2 % 10 = 2
    left = right -> true
    taking middle digit: (2%1)//10 = 0
    reducing div by two digits: 1/100 = 0.01
    at third iteration: x is now 0, thus while x: ends and we return True.
    Case for 1221 will be simillar but here we can learn why divisor needs to be reduced by two digits.
    for (b): div = 1, x = 1221
    we take left by dividing 1221 with 1000.
    1_221 = 1221 // 1000 = 1(from left)
    right by moduolo 10
    122_1 % 10 = 1
    if left != right: false, since 1=1: true
    taking middle digit = (1_22_1%1000)->221//10->22
    if total digits is n, then after removing two digits we have n-2 digits left.
    thus reducing divisor by two digits.
    1000 / 100 = 10^(n-2)
    '''
# @lc code=end

