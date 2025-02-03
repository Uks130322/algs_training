# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        head = None

        while list1 and list2:
            if not head:
                if list1.val <= list2.val:
                    merged = list1
                    list1 = list1.next
                else:
                    merged = list2
                    list2 = list2.next
                head = merged
                continue
            if list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
                merged = merged.next
            else:
                merged.next = list2
                list2 = list2.next
                merged = merged.next
        if merged:
            merged.next = list1 or list2
        return head or list1 or list2