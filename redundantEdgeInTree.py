class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n + 1)

        def find(tmp):
            p = parent[tmp]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a, b):
            p1, p2 = find(a), find(b)

            if p1 == p2:
                return False
            
            if rank[a] > rank[b]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]