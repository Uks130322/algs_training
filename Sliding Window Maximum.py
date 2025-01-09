# https://leetcode.com/problems/sliding-window-maximum/description/
import heapq
from collections import deque


# class MaxForSteam:
#     def __init__(self):
#         self.heap = []
#         self.for_del = dict()
#
#     def add_num(self, num):
#         heapq.heappush(self.heap, -num)
#
#     def del_num(self, num):
#         if self.heap:
#             if self.heap[0] == -num:
#                 heapq.heappop(self.heap)
#             else:
#                 self.for_del[num] = self.for_del.get(num, 0) + 1
#
#     def get_max(self):
#         if self.heap:
#             while True:
#                 if -self.heap[0] in self.for_del:
#                     deleted = -heapq.heappop(self.heap)
#                     self.for_del[deleted] -= 1
#                     if self.for_del[deleted] == 0:
#                         self.for_del.pop(deleted)
#                 else:
#                     return -self.heap[0]
#
#
# def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#     window = MaxForSteam()
#     result = []
#     for i in range(len(nums)):
#         if i < k - 1:
#             window.add_num(nums[i])
#         else:
#             window.add_num(nums[i])
#             result.append(window.get_max())
#             window.del_num(nums[i - k + 1])
#     return result


def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    result = []
    maxes = deque()
    for index, num in enumerate(nums):
        # print(index, num, maxes, result)
        while maxes and num > maxes[-1]:
            maxes.pop()
        # print(index, num, maxes, result)

        maxes.append(num)
        if index >= k - 1:
            result.append(maxes[0])
            if nums[index - k + 1] == maxes[0]:
                maxes.popleft()
        # print(index, num, maxes, result)
    # result += maxes
    return result




print(maxSlidingWindow(0, [1,3,-1,-3,5,3,6,7], k = 3))
print(maxSlidingWindow(0, [1, -1], k = 1))