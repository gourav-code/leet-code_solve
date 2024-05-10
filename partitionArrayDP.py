class Solution:
    def canPartition(self, nums: [int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False

        dp = set()
        dp.add(0)
        target = target // 2
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for tmp in dp:
                if tmp+nums[i] == target:
                    return True
                nextDP.add(tmp+nums[i])
                nextDP.add(tmp)
            dp = nextDP

        return True if target in dp else False
        