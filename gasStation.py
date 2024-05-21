class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        total = 0
        i = 0

        for tmp,value in enumerate(gas):
            total += value - cost[tmp]
            if total < 0:
                total = 0
                i = tmp+1

        return i
##Below soluton is inspired by max Sum of Subarray question but it is slow and above one is fast            
# class Solution:
#     def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
#         diff = []
#         if sum(gas) < sum(cost):
#             return -1

#         for tmp1, tmp2 in zip(gas,cost):
#             diff.append(tmp1-tmp2)

#         Sum = diff[0]
#         val = diff[0]
#         i,j = 0,0

#         for tmp,value in enumerate(diff[1:]):
#             if value > Sum+value:
#                 Sum = value
#                 i = tmp+1
#             else:
#                 Sum += value
#             val = max(val,Sum)

#         return i
            
temp = Solution()
print(temp.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))