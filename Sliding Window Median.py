# # https://leetcode.com/problems/sliding-window-median/description/
#
#
# def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
#     result = []
#     if k == 1:
#         return nums
#     interval = sorted(nums[:k])
#     result.append((interval[k // 2] + interval[k // 2 + (k % 2 - 1)]) / 2)
#     i = k
#     while i < len(nums):
#         out = nums[i - k]
#         add = nums[i]
#         j = 0
#         for j in range(k):
#             # print(interval[j], out)
#             if interval[j] == out:
#                 # print(interval)
#                 interval = interval[:j] + interval[j + 1:]
#                 break
#         for j in range(k - 1):
#             # print(interval, result)
#             if interval[j] <= add:
#                 if j < k - 2:
#                     if interval[j + 1] > add:
#                         interval = interval[:j + 1] + [add] + interval[j + 1:]
#                         break
#                     else:
#                         continue
#                 else:
#                     interval.append(add)
#                     break
#             else:
#                 interval = interval[:j] + [add] + interval[j:]
#                 break
#
#         result.append((interval[k // 2] + interval[k // 2 + (k % 2 - 1)]) / 2)
#         i += 1
#
#     return result
import heapq


class MedianFinder:
    import heapq
    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.left_del = dict()
        self.right_del = dict()
        self.left_del_len = 0
        self.right_del_len = 0

    def addNum(self, num: int) -> None:
        if not self.left_heap:
            if not self.right_heap:
                heapq.heappush(self.left_heap, -num)
            else:
                if num <= self.right_heap[0]:
                    heapq.heappush(self.left_heap, -num)
                else:
                    rigth_top = heapq.heappop(self.right_heap)
                    heapq.heappush(self.right_heap, num)
                    heapq.heappush(self.left_heap, -rigth_top)
            return
        if not self.right_heap:
            if num >= -(self.left_heap[0]):
                heapq.heappush(self.right_heap, num)
            else:
                left_top = -(heapq.heappop(self.left_heap))
                heapq.heappush(self.left_heap, -num)
                heapq.heappush(self.right_heap, left_top)
            return
        if len(self.left_heap) - self.left_del_len == len(self.right_heap) - self.right_del_len:
            if num > -(self.left_heap[0]):
                heapq.heappush(self.right_heap, num)
            else:
                heapq.heappush(self.left_heap, -num)
        elif len(self.left_heap) - self.left_del_len > len(self.right_heap) - self.right_del_len:
            if num > -(self.left_heap[0]):
                heapq.heappush(self.right_heap, num)
            else:
                left_top = -(heapq.heappop(self.left_heap))
                heapq.heappush(self.left_heap, -num)
                heapq.heappush(self.right_heap, left_top)
        else:
            if num > self.right_heap[0]:
                rigth_top = heapq.heappop(self.right_heap)
                heapq.heappush(self.right_heap, num)
                heapq.heappush(self.left_heap, -rigth_top)
            else:
                heapq.heappush(self.left_heap, -num)
        self.balance()

    def delNum(self, num):
        if num == -self.left_heap[0]:
            heapq.heappop(self.left_heap)
        elif num == self.right_heap[0]:
            heapq.heappop(self.right_heap)
        elif num < -self.left_heap[0]:
            self.left_del[num] = self.left_del.get(num, 0) + 1
            self.left_del_len += 1
        elif num > self.right_heap[0]:
            self.right_del[num] = self.right_del.get(num, 0) + 1
            self.right_del_len += 1
        self.balance()

    def balance(self):
        if len(self.left_heap) - self.left_del_len - len(self.right_heap) + self.right_del_len == 2:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        elif len(self.right_heap) - self.right_del_len - len(self.left_heap) + self.left_del_len == 2:
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
        while True:
            if self.left_heap and -self.left_heap[0] in self.left_del:
                peak = heapq.heappop(self.left_heap)
                self.left_del[-peak] -= 1
                self.left_del_len -= 1
                if self.left_del[-peak] == 0:
                    self.left_del.pop(-peak)
            elif self.right_heap and self.right_heap[0] in self.right_del:
                peak = heapq.heappop(self.right_heap)
                self.right_del[peak] -= 1
                self.right_del_len -= 1
                if self.right_del[peak] == 0:
                    self.right_del.pop(peak)
            else:
                break

    def findMedian(self) -> float:
        if len(self.left_heap) - self.left_del_len == len(self.right_heap) - self.right_del_len:
            return (self.right_heap[0] - self.left_heap[0]) / 2
        elif len(self.left_heap) - self.left_del_len < len(self.right_heap) - self.right_del_len:
            return self.right_heap[0]
        else:
            return -self.left_heap[0]

    def __str__(self):
        return f'{self.left_heap}, {self.left_del}\n {self.right_heap}, {self.right_del}'


def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
    result = []
    finder = MedianFinder()
    for i in range(len(nums)):
        if i < k - 1:
            finder.addNum(nums[i])
        else:
            finder.addNum(nums[i])
            result.append(finder.findMedian())
            print(finder)
            print('result: ', result)
            finder.delNum(nums[i - k + 1])
    return result



# obj = MedianFinder()
# obj.addNum(1)
# print(obj)
# obj.addNum(2)
# print(obj)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj)
# print(obj.findMedian())
# obj.addNum(0)
# print(obj)
# print(obj.findMedian())
# obj.addNum(4)
# print(obj)
# print(obj.findMedian())
# obj.delNum(0)
# print(obj)
# print(obj.findMedian())
#
# print(medianSlidingWindow(0, nums = [1,3,-1,-3,5,3,6,7], k = 3))
# print(medianSlidingWindow(0, nums = [1,2,3,4,2,3,1,4,2], k = 3))
# print(medianSlidingWindow(0, nums = [7,0,3,9,9,9,1,7,2,3], k = 6))
print(medianSlidingWindow(0, nums = [-2147483648,-2147483648,2147483647,-2147483648,1,3,-2147483648,-100,8,17,22,
                                     -2147483648,-2147483648,2147483647,2147483647,2147483647,2147483647,-2147483648,
                                     2147483647,-2147483648], k = 6))
# print(medianSlidingWindow(0, nums = [1,4,2,3], k = 4))
# print(medianSlidingWindow(0, nums = [1,2], k = 1))