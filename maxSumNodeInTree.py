def maxPathSum( root: [TreeNode]) -> int:
    res = [root.val]

    def dfs(root):
        if not root:
            return 0

        leftVal = dfs(root.left)
        rightVal = dfs(root.right)
        leftVal = max(leftVal,0)
        rightVal = max(rightVal,0)
        res[0] = max(res[0],root.val+leftVal+rightVal)


        return root.val + max(rightVal,leftVal)

    dfs(root)
    return res[0]