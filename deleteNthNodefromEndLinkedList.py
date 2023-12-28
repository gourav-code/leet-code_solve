def removeNthFromEnd(head: [ListNode], n: int) -> Optional[ListNode]:
    dummy=prev=ListNode()
    dummy.next=right=head
    i=1
    while(i<=n and right):
        right=right.next
        i+=1
    
    while(right):
        prev=prev.next
        right=right.next

    prev.next=prev.next.next

    return dummy.next