#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        #Problem explanation: We need to find the square root of x and return the integer. The problem is that we can't use pow() or ** operator. We can only use alternative way which is binary search. We set left and right pointers, and we keep dividing the range until we find the integer square root.We divide the range
        if not x:
            return  0
        left, right = 1, x
        while left < right:
            mid = left + (right - left) // 2 #formula to prevent overflow
            #mid = (left + right) // 2 -> this can cause overflow in some languages
            #we make sure to subract left from the 
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid
        return left - 1
# @lc code=end

