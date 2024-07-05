class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        if not root:
            return []
            
        left = []
        right = []
        levelNode = deque()
        levelNode.append([root, 0])
        seen = set()
        
        while levelNode:
            for i in range(len(levelNode)):
                root, v = levelNode.popleft()
                if v not in seen:
                    if v < 0:
                        left.append(root.data)
                    else:
                        right.append(root.data)
                    seen.add(v)
                if root.left:
                    levelNode.append([root.left, v-1])
                if root.right:
                    levelNode.append([root.right, v+1])
        
        return left[::-1] + right