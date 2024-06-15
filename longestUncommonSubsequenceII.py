class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        l = defaultdict(list)
        result = -1

        for i,tmp in enumerate(strs):
            l[tmp].append(i)

        for i,tmp in enumerate(strs):
            if len(l[tmp]) > 1:
                continue
            result = max(result, len(tmp))

        return result

        
temp = Solution()
print(temp.findLUSlength())