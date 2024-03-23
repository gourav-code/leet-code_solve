class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()
            for s,d,p in flights: 
                if prices[s] == float("inf"):
                    continue
                if prices[s]+p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            print(tmpPrices)


        return -1 if prices[dst] == float("inf") else prices[dst]


tmp = Solution()
print(tmp.findCheapestPrice(4, [[0,1,1], [1,2,2], [2,3,3]], 0, 3, 1))