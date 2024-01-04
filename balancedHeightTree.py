
def isBalanced(root: [TreeNode]) -> bool:

    def height(root):
        if not root:
            return [True, 0]

        leftHeight=height(root.left)
        rightHeight=height(root.right)
        balanced=leftHeight[0] and rightHeight[0] and abs(leftHeight[1]-rightHeight[1])<=1

        return [balanced, max(leftHeight[1],rightHeight[1])+1]

    return height(root)[0]