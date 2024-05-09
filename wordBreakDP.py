class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        n = len(s)
        j = n-1
        while(j>=0):
            for w in wordDict:
                if (j+len(w) <= len(s) and s[j: j+len(w)] == w):
                    dp[j] = dp[j+len(w)]
                if dp[j]:
                    break

            j -= 1

        return dp[0]
