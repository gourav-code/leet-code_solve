'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        fast, slow = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                break
        
        if not fast or not fast.next:
            return 0
            
        curr = slow.next
        node_len = 1
        while curr != slow:
            node_len += 1
            curr = curr.next
        
        pointer1, pointer2 = head, head
        for _ in range(node_len):
            pointer2 = pointer2.next
            
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        startLoop = pointer1
        
        while startLoop != pointer1.next:
            pointer1  = pointer1.next
            
        pointer1.next = None
            
        return 1
