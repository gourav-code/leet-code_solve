class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            tmp = (n >> i) & 1
            ans = ans | bit << (31-i)

        return ans

##above solution takes n as integer and below solution takes n as string
# class Solution:
#     def reverseBits(self, n: str) -> int:
#         ans = 0
#         m = str(n)
#         for i, tmp in enumerate(m):
#             ans += int(tmp)*2**(i)

#         return ans

        
temp = Solution()
print(temp.reverseBits('11111111111111111111111111111101'))


