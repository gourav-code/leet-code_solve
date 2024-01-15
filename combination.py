
def combinationSum(candidates: [int], target: int) -> [[int]]:
    result = []
    subset = []

    def dsf(i, subset, total):
        if total == target:
            result.append(subset.copy())
            return
        if i >= len(candidates) or total > target:
            return

        subset.append(candidates[i])
        dsf(i ,subset ,total + candidates[i])
        subset.pop()
        dsf(i + 1, subset, total)

    dsf( 0, [], 0)
    return result