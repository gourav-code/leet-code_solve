def maximalSquare(mat):
    if not mat or not mat[0]:
        return 0

    n = len(mat)
    m = len(mat[0])
    
    # Initialize DP matrix
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    
    # Fill DP matrix
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side

# Example usage
mat = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print(maximalSquare(mat))  # Output: 2
