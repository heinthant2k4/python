#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff],i]
            map[n] = i
        return []
# @lc code=end

