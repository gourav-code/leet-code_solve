#User function Template for python3
from typing import List
import heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adjList = { i:[] for i in range(n+1) }
        
        for from_, to_, weight in edges:
            adjList[from_].append([weight, to_])
            adjList[to_].append([weight, from_])
            
        
        # q = deque()
        # q.append([0, 1])
        minHeap = []
        heapq.heapify(minHeap)
        visit = set()
        heapq.heappush(minHeap, [ 0, 1])
        
        while minHeap:
            tmp = heapq.heappop(minHeap)
            if tmp[-1] == n:
                return tmp
            if tmp[-1] not in visit:
                visit.add(tmp[-1])
                for tmp_weight, tmp_node in adjList[tmp[-1]]:
                    temp = tmp.copy()
                    temp.append(tmp_node)
                    temp[0] += tmp_weight
                    heapq.heappush(minHeap, temp)
                
        return [-1]