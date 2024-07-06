class Solution:
    def longestCommonPrefix(self, n, arr):
        # code here
        arr = sorted(arr)
        start = arr[0]
        end = arr[len(arr)-1]
        ans = ''
        for i in range(min(len(start), len(end))):
            if start[i] != end[i]:
                break
            ans += start[i]
            
        if len(ans) == 0:
            return '-1'
        
        return ans