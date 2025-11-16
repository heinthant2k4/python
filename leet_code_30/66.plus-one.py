#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Simple grade school addition with carry method. We start from the last digit and add one. If the sum is less than 10, we return the digits. If the sum is 10, we set the current digit to 0 and carry 1 to the next digit. If we finish the loop and still have a carry, we insert 1 at the beginning of the list.
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i]=0
            if i == 0:
                return [1] + digits
# @lc code=end

