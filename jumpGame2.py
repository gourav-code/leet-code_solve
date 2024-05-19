##  array can be seen as in levels with first element being only element in first level and 
##  other level are divided based on  next of last element on previous level and farthest element can 
##  be reached from previous level
class Solution:
    def jump(self, nums: [int]) -> int:
        l =r = 0
        result = 0

        while r < len(nums)-1:
            tmp = 0
            for i in range(l,r+1):
                tmp = max(tmp, i+nums[i])
            l = r+1
            r = tmp
            result += 1

        return result