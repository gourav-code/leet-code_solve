class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        l = [amount+1]*(amount+1)  #amount +1 is max int for this question we can also use another max int and that from 0 ... amount
        l[0] = 0

        for i in range(1, amount+1):
            for tmp in coins:
                if i-tmp >= 0:
                    l[i] = min(l[i], 1 + l[i-tmp])

        return l[amount] if l[amount] != amount+1 else -1
        

tmp = Solution()
print(tmp.coinChange(coins = [3], amount = 4))