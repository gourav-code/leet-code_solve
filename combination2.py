
def combinationSum2( candidates: [int], target: int) -> [[int]]:
    result = []
    subset = []
    candidates.sort()

    def dsf(i, total):
        if total == target :
            result.append(subset[:])
            return
        if i >= len(candidates) or total > target:
            return
        prev = -1
        for j in range(i, len(candidates)):
            if candidates[j] == prev:
                continue
            subset.append(candidates[j])
            dsf(j+1, total + candidates[j])
            subset.pop()
            prev = candidates[j]
        

    dsf(0, 0)
    return result