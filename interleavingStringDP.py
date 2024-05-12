class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n = len(s1)
        m = len(s2)
        l = len(s3)

        if(l != n+m):
            return False

        dp = {}
        i, j, k = 0, 0, 0

        def dfs(i, j, k):
            if k==l and i==n and j==m:
                return True
            if (i,j,k) in dp:
                return False
            if i<n and s3[k] == s1[i] and dfs(i+1, j, k+1):
                return True
            if j< m and s3[k] == s2[j] and dfs(i, j+1, k+1):
                return True
            dp[(i,j,k)] = False
            return False
            
        return dfs(0,0,0)

tmp = Solution()
print(tmp.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))