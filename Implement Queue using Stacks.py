# https://leetcode.com/problems/implement-queue-using-stacks/description/

from collections import deque


class MyQueue:
    from collections import deque

    def __init__(self):
        self._queue = deque()

    def push(self, x: int) -> None:
        self._queue.append(x)

    def pop(self) -> int:
        return self._queue.popleft()

    def peek(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return len(self._queue) == 0

    # Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()