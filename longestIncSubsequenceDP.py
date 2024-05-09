class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    dp[i] = max(1+dp[j],dp[i])
        
        print(dp)
        return max(dp)

tmp = Solution()
print(tmp.lengthOfLIS([10,9,2,5,3,7,101,18]))