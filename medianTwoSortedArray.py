class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        low, high = 0, n1
        left = (n1+n2+1)//2
        n = n1 + n2
        while low <= high:
            mid = (low+high)>>1
            mid2 = left - mid
            l1,l2,r1,r2 = 0,0,0,0
            r1 = nums1[mid] if mid < n1 else float('inf')
            l1 = nums1[mid-1] if mid-1 >= 0 else float('-inf')
            l2 = nums2[mid2-1] if mid2-1 >= 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < n2 else float('inf')
            if (l1 <= r2 and l2 <= r1):
                if n%2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return float(max(l1,l2))
            if l1 > r2:
                high = mid-1
            if l2 > r1:
                low = mid+1
                
        return 0.00
        

        
                

temp = Solution()
print(temp.findMedianSortedArrays([1,3],[2]))