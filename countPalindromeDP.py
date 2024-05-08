class Solution:
    def countSubstrings(self, s: str) -> int:
        result_len = 0
        result = ""
        n = len(s)
        num = 0
        for i in range(n):
            #odd len
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                num += 1
                result = s[l:r+1]
                print(f"odd: {result}")
                l -= 1
                r += 1

            #even len
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                num += 1
                result = s[l:r+1]
                print(f"even: {result}")
                l -= 1
                r += 1

        return num


tmp = Solution()
print(tmp.countSubstrings("aaa"))