#The width of one level is defined as the length between the end-nodes
# (the leftmost and rightmost non-null nodes), 
# where the null nodes between the end-nodes that would be present in a complete binary tree
# leetcode problem 662
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        ans = 0
        levelNode = deque()
        levelNode.append([root, 0])
        
        while levelNode:
            n = len(levelNode)
            firstID, lastID = 0, 0
            levelMin = levelNode[0][1]
            for i in range(n):
                node, curID = levelNode.popleft()
                curID -= levelMin
                if i == 0:
                    firstID = curID
                if i == n-1:
                    lastID = curID
                if node.left:
                    levelNode.append([node.left, 2*curID+1])
                if node.right:
                    levelNode.append([node.right, 2*curID+2])
            ans = max(ans, lastID - firstID + 1)
            
        return ans
        