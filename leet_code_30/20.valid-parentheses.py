#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Since we need a pair, string length must be even. If odd, return False.
        we will create a dictionary to map opening and closing brackets.
        key as opening bracket and value as closing bracket.
        we will use a stack to keep track of opening brackets.
        we will iterate through the string character by character.
        if the character is an opening bracket, we will push it onto the stack.
        if the character is a closing bracket,
        then we will check if the stack is not empty and if the top of the stack(last item) matches its key pair.
        if it matches, we will pop the top of the stack.
        if it doesn't match or stack is empty, we will return False.
        at the end of iteration, if the stack is empty, we will return True, else False.
        '''
        if len(s) % 2 != 0:
            return False
        bracket_map = {
            '(' : ')',
            '{' : '}',
            '[': ']'
        }
        stack = []
        for char in s:
            if char in bracket_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if bracket_map[top] != char:
                        return False
        return len(stack) == 0

# @lc code=end

