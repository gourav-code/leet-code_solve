def mergeList(self, l1, l2):
    dummy=ListNode()
    tail=dummy

    while(l1 and l2):
        if(l1.val<l2.val):
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail=tail.next

    if(l1):
        tail.next=l1
    elif(l2):
        tail.next=l2

    return dummy.next


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if(not lists and len(lists)==0):
        return None

    while(len(lists)>1):
        mergedList=[]
        for i in range(0,len(lists),2):
            l1=lists[i]
            l2=lists[i+1] if (i+1)<len(lists) else None
            mergedList.append(self.mergeList(l1,l2))
        lists=mergedList

    return lists[0]