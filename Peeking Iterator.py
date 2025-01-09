# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.temp = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext():
            if not self.temp:
                self.temp = self.iterator.next()
            return self.temp


    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if self.temp:
                result = self.temp
                self.temp = None
                return result
            else:
                return self.iterator.next()


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.iterator.hasNext() or self.temp:
            return True
        else:
            return False


# Your PeekingIterator object will be instantiated and called as such:
# nums = [1,2,3]
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     print(val, iter.next())         # Should return the same value as [val].