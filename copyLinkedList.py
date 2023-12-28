def copyRandomList(head: [Node]) -> [Node]:
    mapNodeCopy={None:None}

    cur=head
    while(cur):
        newNode=Node(cur.val,None,None)
        mapNodeCopy[cur]=newNode
        cur=cur.next

    cur=head
    while(cur):
        copy=mapNodeCopy[cur]
        copy.next=mapNodeCopy[cur.next]
        copy.random=mapNodeCopy[cur.random]
        cur=cur.next

    return mapNodeCopy[head]