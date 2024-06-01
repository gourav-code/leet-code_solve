##There is one more solution with sum of whole number = n*(n+1)/2 - sum of
# num in array
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            ans ^= i^nums[i]
        ans ^= n
        return ans

temp = Solution()
print(temp.missingNumber([0,1]))        

##Below one is my solution
# class Solution:
#     def missingNumber(self, nums: [int]) -> int:
#         n = len(nums)
#         for i in range(n+1):
#             nums.append(i)

#         ans = 0
#         for tmp in nums:
#             ans = ans^tmp
        
#         return ans
        