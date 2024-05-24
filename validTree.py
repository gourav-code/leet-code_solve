class Solution:
    def validTree(self, n: int, edges: [[int]]) -> bool:
        if not n:
            return True

        l = {i:[] for i in range(n)}
        for key, val in edges:
            l[key].append(val)
            l[val].append(key)

        visit = set()
        
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for tmp in l[i]:
                if prev == tmp:
                    continue
                
                if not dfs(tmp, i):
                    return False
            
            return True

        return dfs(0,-1) and len(visit) == n


        