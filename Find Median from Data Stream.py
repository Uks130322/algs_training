# https://leetcode.com/problems/find-median-from-data-stream/description/
import heapq


class MedianFinder:
    import heapq
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

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
        if len(self.left_heap) == len(self.right_heap):
            if num > -(self.left_heap[0]):
                heapq.heappush(self.right_heap, num)
            else:
                heapq.heappush(self.left_heap, -num)
        elif len(self.left_heap) > len(self.right_heap):
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

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (self.right_heap[0] - self.left_heap[0]) / 2
        elif len(self.left_heap) < len(self.right_heap):
            return self.right_heap[0]
        else:
            return -self.left_heap[0]

    def __str__(self):
        return f'{self.left_heap}, {self.right_heap}'


obj = MedianFinder()
obj.addNum(1)
print(obj)
obj.addNum(2)
print(obj)
print(obj.findMedian())
obj.addNum(3)
print(obj)
print(obj.findMedian())
obj.addNum(0)
print(obj)
print(obj.findMedian())
obj.addNum(4)
print(obj)
print(obj.findMedian())