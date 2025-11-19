#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Problem explanation: We are given a digit of arrays and solution requires us to return after adding large integer by one. This is just grade school math, if last digit is less than 9 -> we can just add one and return. If last digit is 9 combined is 10 so carry is 1 and digit is 0. We continue this process until we finish the array or there is no carry.
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
# @lc code=end

