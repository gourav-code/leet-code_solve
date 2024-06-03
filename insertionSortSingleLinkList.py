# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(float('-inf'), None)

        while head:
            tmp = head.next
            temp = dummyHead

            while(temp.next and temp.next.val < head.val):
                temp = temp.next

            head.next = temp.next
            temp.next = head
            head = tmp

        return dummyHead.next

        