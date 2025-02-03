# https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """Both solutions work correctly"""
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first = 0
        # second = 0
        # pow1 = 0
        # pow2 = 0
        # while l1:
        #     first += l1.val * 10 ** pow1
        #     pow1 += 1
        #     l1 = l1.next
        # while l2:
        #     second += l2.val * 10 ** pow2
        #     pow2 += 1
        #     l2 = l2.next
        # summa = first + second
        # peak = ListNode(val=summa % 10)
        # result = peak
        # summa //= 10
        # while summa:
        #     result.next = ListNode(val=summa % 10)
        #     result = result.next
        #     summa //= 10
        # return peak
        result = None
        head = None
        over = 0
        while l1 and l2:
            if not result:
                result = ListNode(val=(l1.val + l2.val + over) % 10)
                head = result
            else:
                result.next = ListNode(val=(l1.val + l2.val + over) % 10)
                result = result.next
            over = (l1.val + l2.val + over) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            result.next = ListNode(val=(l1.val + over) % 10)
            over = (l1.val + over) // 10
            result = result.next
            l1 = l1.next
        while l2:
            result.next = ListNode(val=(l2.val + over) % 10)
            over = (l2.val + over) // 10
            result = result.next
            l2 = l2.next
        if over:
            result.next = ListNode(over)
        return head

