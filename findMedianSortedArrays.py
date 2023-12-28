def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    arr=[]
    n1_l=n2_l=0
    n1_r,n2_r=len(nums1),len(nums2)

    while(n1_l<n1_r and n2_l<n2_r):
        if(nums1[n1_l]<nums2[n2_l]):
            arr.append(nums1[n1_l])
            n1_l+=1
        else:
            arr.append(nums2[n2_l])
            n2_l+=1

    while(n1_l==n1_r and n2_l<n2_r):
        arr.append(nums2[n2_l])
        n2_l+=1
    
    while(n2_l==n2_r and n1_l<n1_r):
        arr.append(nums1[n1_l])
        n1_l+=1

    n=len(arr)
    print(arr)

    if(n%2!=0):
        return float(arr[(n//2)])
    else:
        return float((arr[(n-1)//2]+arr[n//2])/2)

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))