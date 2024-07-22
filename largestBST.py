class Solution:
    def largestBst(self, root):
        # Your code here
        if not root:
            return 0
        
        size = [0]
        
        def dfs(root):
            if not root:
                return [True, 0, float('-inf'), float('inf')]
            
            leftAns = dfs(root.left)
            rightAns = dfs(root.right)
            
            if leftAns[0] and rightAns[0] and leftAns[2] < root.data < rightAns[3]:
                curSize = leftAns[1]+rightAns[1]+1
                return [True, curSize, max(rightAns[2],root.data), min(root.data, leftAns[3])]
            else:
                return [False, max(leftAns[1],rightAns[1]), 0, 0 ]
                
        result = dfs(root)
        
        return result[1]