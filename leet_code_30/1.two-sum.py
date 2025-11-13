#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[2,7,11,15] -> [2,7|.11.15]
        #hashmap
        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num # x = 9 - 2 = 7-> 7 in prevMap.
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i #{} -> 2:0 -> 7:1->11:2
        return []
        
# @lc code=end

