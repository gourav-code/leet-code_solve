class Solution:
    #Think first about small weight limit and then small vals array
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = [[0]*(n+1) for _ in range(W+1)]
        
        for i in range(1,W+1):
            for j in range(n-1,-1,-1):
                tmp = 0
                if i-wt[j]>=0:
                    tmp = val[j]+dp[i-wt[j]][j+1]
                dp[i][j] = max(tmp,dp[i][j+1],dp[i-1][j])
                
        return dp[W][0]