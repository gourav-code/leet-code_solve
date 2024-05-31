class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n%2
            n = n >> 1
        return ans
        
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         count = 0
#         ans = 0
#         # l = {}
#         loop = True
#         while loop:
#             if 2**count > n:
#                 ans += 1
#                 # loop = False
#                 break
#             # l[count] = 2**count
#             count += 1
#         # print(f"n: {n},count: {count}, m : {n-2**(count-1)}")
#         # print(l)
#         m = n-2**(count -1)
#         ans += self.hammingWeight(m)
#         return ans                

temp = Solution()
print(temp.hammingWeight(2147483645))