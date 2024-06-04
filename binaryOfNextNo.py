class Solution:
    def binaryNextNumber(self, s):
        # code here
        n = 0
        ans = ''
        carry = 1
        for i, tmp in enumerate(s[::-1]):
            ans += str(int(tmp) ^ carry)
            carry = int(tmp) & carry

        if carry:
            ans += str(carry)
            
        ans = ans[::-1]
            
        for i, tmp in enumerate(ans):
            if tmp == '1':
                ans = ans[i:]
                break
        return ans

temp = Solution()
print(temp.binaryNextNumber('01111'))