
def subsets( nums: [int]) -> [[int]]:
    result = []
    subset = []

    def dsf(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dsf(i+1)

        subset.pop()
        dsf(i+1)

    dsf(0)

    return result


print(subsets([1,5,7]))