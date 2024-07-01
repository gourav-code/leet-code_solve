from collections import deque
#Function to make binary tree from linked list.
def convert(head):
  
    # code here
    if not head:
        return None
        
    count, i = 1, 1
    root = Tree(head.data)
    stack = deque()
    stack.append(root)
    head = head.next
    
    while head:
        prev_i = i
        i += 2**count
        count += 1
        while head and stack and prev_i < i:
            node = stack.popleft()
            if head:
                tmp = Tree(head.data)
                node.left = tmp
                stack.append(tmp)
                head = head.next
                
            if head:
                tmp = Tree(head.data)
                node.right = tmp
                stack.append(tmp)
                head = head.next
                
            prev_i += 1
            
    return root
