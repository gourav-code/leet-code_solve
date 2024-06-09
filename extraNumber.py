class Solution:
    def findExtra(self,n,a,b):
        #add code here
        l, r = 0, n-1
        
        while l<r:
            mid = (l+r)//2
            if a[mid] == b[mid]:
                l = mid+1
            else:
                r = mid

        return l

temp = Solution()
print(temp.findExtra(7, [2,3,4,6,8,10,12], [2,4,6,8,10,12]))