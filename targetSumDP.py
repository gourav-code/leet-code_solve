class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        dp = {}

        def dfs(i, a):
            if(i==len(nums) and a == target):
                return 1
            if(i >= len(nums)):
                return 0
            if (i, a) in dp:
                return dp[(i, a)]

            dp[(i, a)] = dfs(i+1, a+nums[i]) + dfs(i+1, a - nums[i])
            return dp[(i,a)]
        
        return dfs(0, 0)

l = Solution()
print(l.findTargetSumWays(nums = [1,1,1,1,1], target = 3))