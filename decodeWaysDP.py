class Solution:
    def numDecodings(self, s: str) -> int:
        chase = {len(s) : 1}

        def dfs(i):
            if i in chase:
                return chase[i]
            if s[i] == "0":
                return 0

            result = dfs(i+1)

            if (i+1 < len(s) and 10 <= int(s[i:i+2]) and int(s[i:i+2]) <= 26):
                result += dfs(i+2)

            chase[i] = result

            return result

        return dfs(0)