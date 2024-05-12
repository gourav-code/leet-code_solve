class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        dp = {}

        def dfs(i, a):
            if len(coins) == i:
                return 0
            if a > amount:
                return 0
            if (i, a) in dp:
                return dp[(i, a)]
            if a == amount:
                return 1

            dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i+1, a)
            return dp[(i, a)]

        return dfs(0, 0)