# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next}"

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        last = None
        while fast != None and fast.next != None:
            last = slow
            slow = slow.next
            fast = fast.next.next

        last.next = self.reverse(slow)

        curr = head
        twin = last.next
        best = 0
        while twin != None:
            best = max(best, curr + twin)
            curr = curr.next
            twin = twin.next
        return best

    def reverse(self, head):
        curr = head
        nx = curr.next
        curr.next = None
        while nx != None:
            last = curr
            curr = nx
            nx = curr.next
            curr.next = last

        head.next = None
        return head

def buildListNode(x: list):
    head = ListNode()
    curr = head
    for i in x:
        curr.val = i
        curr.next = ListNode()
        curr = curr.next

    return head


print(Solution().reverse(buildListNode([1, 2, 3, 4, 5])))

