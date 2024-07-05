def verticalWidth(root):
    # code here
    if not root:
        return 0
        
    levelNode = deque()
    levelNode.append([root, 0, 0]) #[root, vertical, level]
    low, high = 0, 0
    while levelNode:
        n = len(levelNode)
        for i in range(n):
            root, v, l = levelNode.popleft()
            low = min(low, v)
            high = max(v, high)
            if root.left:
                levelNode.append([root.left, v-1, l+1])
            if root.right:
                levelNode.append([root.right, v+1, l+1])
    
        
    return high-low+1