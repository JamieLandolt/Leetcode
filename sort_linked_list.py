from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        this = head
        prev = None
        while head != None and head.next != None:
            while this != None and this.next != None:
                if this.val > this.next.val:
                    self.swap(prev, this, this.next)
                prev = this
                this = this.next
            head = head.next
        return head

    def swap(self, prev, this, next):
        if prev:
            prev.next = next
        if next:
            this.next = next.next
            next.next = this

