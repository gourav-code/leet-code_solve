

def search( nums: [int], target: int) -> int:
    l,r=0,len(nums)-1

    while l<=r:
        tmp=(l+r)//2
        print(f"l:{l} r:{r} tmp:{tmp}")
        if(nums[tmp]==target):
            return tmp
        elif(target>=nums[l] and target<nums[tmp]):
            r=tmp-1
        elif(nums[l]>nums[tmp] and nums[tmp]<target and target>=nums[l]):
            r=tmp-1
        elif(nums[l]>nums[tmp] and nums[tmp]>target):
            r=tmp-1
        else:
            l=tmp+1

    return -1

nums=[5,1,3]
target=3
print(search(nums,target))
print(f"arr:{nums} target:{target}")

