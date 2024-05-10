class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1]*n

        for i in range(m-1):
            currRow = [1]*n
            for j in range(n-2,-1,-1):
                currRow[j] = currRow[j+1] + prevRow[j]

            prevRow = currRow

        return prevRow[0]