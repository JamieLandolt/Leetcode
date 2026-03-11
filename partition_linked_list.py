from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = None
        eq = None
        gt = None
        lt_head = None
        eq_head = None
        gt_head = None
        this = head
        while this != None:
            print(f"Log: {lt_head=} {eq_head=} {gt_head=}")
            if this.val > x:
                if gt == None:
                    gt_head = ListNode(this.val)
                    gt = gt_head
                else:
                    gt.next = ListNode(this.val)
                    gt = gt.next
            if this.val == x:
                if eq == None:
                    eq_head = ListNode(this.val)
                    eq = eq_head
                else:
                    eq.next = ListNode(this.val)
                    eq = eq.next
            if this.val < x:
                if lt == None:
                    lt_head = ListNode(this.val)
                    lt = lt_head
                else:
                    lt.next = ListNode(this.val)
                    lt = lt.next
            this = this.next

        if lt and eq and gt:
            lt.next = eq_head
            eq.next = gt_head
            return lt_head
        elif lt and eq:
            lt.next = eq_head
            return lt_head
        elif lt:
            return lt_head
        elif eq and gt:
            eq.next = gt_head
            return eq_head
        elif eq:
            return eq_head
        elif gt:
            return gt_head
        else:
            print(f"E: {lt_head=} {eq_head=} {gt_head=}")

l = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2, None))))))
print(Solution().partition(l, 3))