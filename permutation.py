
def permute( nums: [int]) -> [[int]]:
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)

        combinations = permute(nums)

        for tmp in combinations:
            tmp.append(n)

        result.extend(combinations)
        nums.append(n)

    return result

print(permute([1,6,8]))