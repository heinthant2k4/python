#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Two pointer method will be used, left is at the start and right is at 1. if left != right, we increment left and set nums[left] = nums[right]. at the end we return left+1 since left is index based.
        left = 0
        for right in range(1,len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1
    '''
    Tracing: input: [0,0,1,1,1,2,2,3,3,4]
    left = 0, right = 1
    right in range(1,10):
    if nums[0] != nums[1]: 0=0 so false
    left is incremented only when left and right are not equal. left is still 0 and rigt is now 2.
    if nums[0] != nums[2]: 0!=1 so true
    left += 1 -> left = 1
    nums[1] = nums[2] -> nums[1] = 1
    and so on
    '''
# @lc code=end

