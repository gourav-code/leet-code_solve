
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#below solution is 1.58
#Second solution is better solution
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # your code here
        
        nodesDetail = {}
        root = None
        
        for i in range(len(parent)):
            if i not in nodesDetail:
                nodesDetail[i] = Node(i)
            
            if parent[i] == -1:
                root = nodesDetail[i]
            else:
                if parent[i] not in nodesDetail:
                    nodesDetail[parent[i]] = Node(parent[i])
                    
                if not nodesDetail[parent[i]].left:
                    nodesDetail[parent[i]].left = nodesDetail[i]
                else:
                    nodesDetail[parent[i]].right = nodesDetail[i]
                    
                    
        return root

#below solution time taken is 1.43
class Solution2:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # your code here
        
        nodesDetail = {}
        root = None
        
        for i in range(len(parent)):
            nodesDetail[i] = Node(i)
            
        for i in range(len(parent)):
            if parent[i] == -1:
                root = nodesDetail[i]
            else:
                    
                if not nodesDetail[parent[i]].left:
                    nodesDetail[parent[i]].left = nodesDetail[i]
                else:
                    nodesDetail[parent[i]].right = nodesDetail[i]
                    
                    
        return root


temp = Solution()

root = temp.createTree([-1, 0, 0, 1, 1, 3, 5])

from collections import deque

q = deque()
q.append(root)
while q:
    for _ in range(len(q)):
        root = q.popleft()
        print(root.key, end=" ")
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

