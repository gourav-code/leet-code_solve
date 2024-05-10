#this question has different thinking process and different solution, don't see code to understand, watch video again dp 2D
#https://www.youtube.com/watch?v=I7j0F7AHpb8
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            coolD = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, coolD)
            else:
                sell = dfs(i+2, not buying) +prices[i]
                dp[(i, buying)] = max(sell, coolD)

            return dp[(i,buying)]

        return dfs(0, True)


tmp = Solution()
print(tmp.maxProfit([1,2,3,0,2]))


        
