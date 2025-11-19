#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Problem requires us to solve the problem with O(log n) complexity, we gonna use sliding window method and divide and conquer algorithm to find the target index.
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            else:
                r -= 1
        return l
# @lc code=end

