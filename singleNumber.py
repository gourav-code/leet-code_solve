# class Solution:
#     def singleNumber(self, nums: [int]) -> int:
#         result_list = []
#         for tmp in nums:
#             if tmp in result_list:
#                 result_list.remove(tmp)
#             else:
#                 result_list.append(tmp)

#         return result_list[0]

# tmp = Solution()
# print(tmp.singleNumber([4,2,1,2,1]))

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for tmp in nums:
            ans = ans^tmp
        return ans