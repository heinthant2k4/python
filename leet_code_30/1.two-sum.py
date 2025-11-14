#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We will keep a mapping to track of the elements, visited nodes will be in the hashmap.
        prevMap = {}
        #enumerate function iterate nums:List with a key:value pair, counter(starts from 0) is the key and iterated element is the value
        for i,num in enumerate(nums):
            #x+y = z
            #we know x and z, y = z-x
            diff = target - num
            #if y is visited then we return y's index and x's index
            if diff in prevMap:
                return [prevMap[diff],i]
            #we add visited node to num value as key
            prevMap[num] = i
        return []

        
# @lc code=end

