#greedy solution
class Solution:
    def canJump(self, nums: [int]) -> bool:
        target = len(nums)-1

        for tmp in range(len(nums)-1,-1,-1):
            if tmp+nums[tmp] >= target:
                target = tmp

        return True if target == 0 else False

#below dynamic solution

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         l = []

#         def dfs(i,jump):
#             if (i,jump) in l or i+jump >= len(nums):
#                 return False

#             if i+jump == len(nums)-1:
#                 return True

#             l.append((i,jump))
#             j = i+jump
#             val = nums[j]

#             for tmp in range(val,0,-1):
#                 if j+tmp == len(nums)-1 or dfs(j,tmp):
#                     return True

#             return False

#         return dfs(0,0)        