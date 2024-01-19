class Solution:
    def __init__(self, s):
        self.s = s

    def isPalindrome(self, s, i, j):
        
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1

        return True

    def partition(self, s: str) -> [[str]]:

        result = []
        subset = []

        def dsf(i):
            if i >= len(s):
                result.append(subset[:])
                return

            for j in range(i, len(s)):
                if self.isPalindrome( s, i, j):
                    subset.append(s[i:j+1])
                    dsf(j+1)
                    subset.pop()
        dsf(0)
        return result


use = Solution("aab")
print(use.partition())