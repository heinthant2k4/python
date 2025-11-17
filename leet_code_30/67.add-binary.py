#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = []
        for i in range(len(a)):
            digit_a = int(a[i])
            digit_b = int(b[i]) if i < len(b) else 0
            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2
        if carry:
            result.append('1')
        return ''.join(result[::-1])
# @lc code=end

