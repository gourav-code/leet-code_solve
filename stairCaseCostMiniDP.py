class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        last = cost[-1]
        second_last = cost[-2]
        i = len(cost) - 3
        while(i>=0):
            ans = min(second_last, last) + cost[i]
            last = second_last
            second_last = ans
            i -= 1

        return min(last, second_last)