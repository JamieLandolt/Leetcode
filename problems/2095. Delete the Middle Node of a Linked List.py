# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_num = 0
        curr = head
        while curr != None:
            node_num += 1
            curr = curr.next

        curr = head
        if node_num == 1:
            return None

        for _ in range(node_num // 2):
            last = curr
            curr = curr.next

        last.next = curr.next
        return head



