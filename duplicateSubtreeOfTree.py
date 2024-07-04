from collections import defaultdict
class Solution:
    def printAllDups(self, root):
        # code here
        l = defaultdict(int)
        ans = []
        def dfs(root):
            if not root:
                return 'N'

            s = str(root.data) + ',' + dfs(root.left) + ',' + dfs(root.right)

            if l[s] == 1:
                ans.append(root)

            l[s] += 1
            return s

        dfs(root)
        # print()
        return ans