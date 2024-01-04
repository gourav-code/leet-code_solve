def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    stack=[]
    top=root
    result=[]

    while(True):
        if(top):
            stack.append(top)
            top=top.left
        else:
            if(len(stack)==0):
                break
            top=stack.pop()
            result.append(top.val)
            top=top.right

    return result