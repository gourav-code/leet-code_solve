class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        maxP = 1
        minP = 1
        res = arr[0]
        for i in range(len(arr)):
            tmp = arr[i]*maxP
            maxP = max(tmp, arr[i], arr[i]*minP, maxP)
            minP = min(tmp, arr[i], arr[i]*minP, minP)
            res = max(maxP,res)
        return res%(10**9+7)