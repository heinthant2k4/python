#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #This problem is quite simillar to remove_duplicates(). In-place -> two pointers method. 
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
    '''
    Tracing: input: nums = [3,2,2,3], val = 3
    left = 0
    right in range(0,4):
    if nums[0] != 3: false
    right = 1
    if nums[1] != 3: true
    nums[0] = nums[1] -> nums[0] = 2
    left += 1 -> left = 1
    right = 2
    if nums[2] != 3: true
    nums[1] = nums[2] -> nums[1] = 2
    left += 1 -> left = 2
    right = 3
    if nums[3] != 3: false
    end of for loop
    return left -> 2
    Resulting nums = [2,2,_,_]
    '''
# @lc code=end

