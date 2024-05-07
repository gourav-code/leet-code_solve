class Solution:
    def rob(self, nums: [int]) -> int:

        first, second = 0, 0

        for tmp in nums:
            temp = max(tmp+first, second)
            first = second
            second = temp

        return second

# Below is another way to solve this problem and above had different thinking process
        # n = len(nums)
        # if(n == 1):
        #     return nums[0]
        # elif(n == 2):
        #     return max(nums[0], nums[1])
        # elif(n == 3):
        #     return max(nums[0]+nums[2], nums[1])
        
        # last = nums[-1]
        # second_last = nums[-2]
        # third_last = last + nums[-3]

        # i = n - 4
        # while(i >=0 ):
        #     tmp = nums[i]+max(last, second_last)
        #     last = second_last
        #     second_last = third_last
        #     third_last = tmp
        #     i -= 1

        # return max(second_last, third_last)


        