class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        minVal, maxVal = 1, 1

        for tmp in nums:
            temp = tmp*maxVal
            maxVal = max(tmp, temp, tmp*minVal)
            minVal = min(tmp, temp, tmp*minVal)
            result = max(result, maxVal)

        return result