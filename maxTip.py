from typing import List


class Solution1:
    def maxTip1(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # Create a list of orders with their respective tips and index
        orders = [(arr[i], brr[i], i) for i in range(n)]
        
        # Sort orders based on the absolute difference in tips (|arr[i] - brr[i]|)
        orders.sort(key=lambda order: abs(order[0] - order[1]), reverse=True)
        
        total_tips = 0
        a_count = 0
        b_count = 0
        
        # Distribute the orders to maximize the tips
        for a_tip, b_tip, i in orders:
            if (a_tip >= b_tip and a_count < x) or b_count >= y:
                total_tips += a_tip
                a_count += 1
            else:
                total_tips += b_tip
                b_count += 1
        
        return total_tips

# Example usage
temp = Solution()
print(temp.maxTip(5, 3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
#Below is dynamic problem

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        dp = {}

        def dfs(i, a, b):
            if i == n:
                return 0

            if (i, a, b) in dp:
                return dp[(i, a, b)]

            res1 = res2 = 0
            if a < x:
                res1 = arr[i] + dfs(i + 1, a + 1, b)
            if b < y:
                res2 = brr[i] + dfs(i + 1, a, b + 1)

            dp[(i, a, b)] = max(res1, res2)
            return dp[(i, a, b)]

        return dfs(0, 0, 0)

# Example usage:
temp = Solution()
print(temp.maxTip(5, 3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
