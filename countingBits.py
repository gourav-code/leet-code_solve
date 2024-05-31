#better and faster solution
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        offset = 1
        for i in range(1,n+1):
            if i == offset*2:
                offset = i
            ans[i] = 1 + ans[i-offset]

        return ans
# class Solution:  #slow solution
#     def countBits(self, n: int) -> [int]:
#         ans = [0] * (n+1)

#         for i in range(n+1):
#             tmp = i
#             while tmp:
#                 tmp = tmp & (tmp-1)
#                 ans[i] += 1

#         return ans

# temp = Solution()
# print(temp.countBits(5))