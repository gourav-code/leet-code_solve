class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        ans = 0
        result = 0
        while(N>0):
            digit = N%2
            if digit == 1:
                ans += 1
            else:
                result = max(result, ans)
                ans = 0
            N //= 2
            
        return max(result,ans)


temp = Solution()
print(temp.maxConsecutiveOnes(14))