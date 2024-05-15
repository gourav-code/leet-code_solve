class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        Sum = nums[0]
        val = nums[0]

        for tmp in nums[1:]:
            if tmp > Sum+tmp:
                Sum = tmp
            else:
                Sum += tmp
            val = max(val, Sum)
            
        return val
        
#Below code is given in video and above one is self
        # def maxSubArray(self, nums: List[int]) -> int:
        # res = nums[0]

        # total = 0
        # for n in nums:
        #     total += n
        #     res = max(res, total)
        #     if total < 0:
        #         total = 0
        # return res