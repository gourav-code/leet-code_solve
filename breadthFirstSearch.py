# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(root: [TreeNode]) -> List[List[int]]:
    q=deque()
    if not root:
        return []
    q.append(root)
    result=[[root.val]]
    while q:
        l=[]
        for i in range(len(q)):
            node=q.popleft()
            if(node.left):
                l.append(node.left.val)
                q.append(node.left)
            if(node.right):
                l.append(node.right.val)
                q.append(node.right)
        
        if(len(l)!=0):
            result.append(l)

    return result
            