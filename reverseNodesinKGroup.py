def tillNodefunc(self,head,tail,k):
    cur=head
    while(cur and tail and k>1):
        tail=tail.next
        k-=1

    return tail

def reverseList(self,head,tail):
    cur,tillNode=head,tail
    prev=None
    tillNode.next=None
    while(head):
        tmp=head.next
        head.next=prev
        prev=head
        head=tmp

    return [cur,tillNode]

def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy=prev=ListNode()
    prev.next=head
    tillNode=cur=head

    while(cur and tillNode):
        tillNode=self.tillNodefunc(cur,tillNode,k)
        if(not tillNode): break
        tillNodetmp=tillNode.next
        cur,tillNow=self.reverseList(cur,tillNode)
        prev.next=tillNode
        cur.next=tillNodetmp
        prev=cur
        cur=cur.next
        tillNode=cur

    return dummy.next