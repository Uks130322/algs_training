# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    previous = None
    while head.next:
        next_item = head.next
        head.next = previous
        previous = head
        head = next_item
    head.next = previous
    return head

def canonical_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        nextHead = head.next
        head.next = prev
        prev, head = head, nextHead
    return prev