# https://leetcode.com/problems/merge-intervals/description/


def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    result = []
    intervals.sort(key=lambda x: x[0])
    for pare in intervals:
        if not result or result[-1][-1] < pare[0]:
            result.append(pare)
        else:
            result[-1][-1] = max(pare[1], result[-1][-1])

    return result


print(merge(1, [[1,3],[2,6],[8,10],[15,18]]))
print(merge(1, [[1,4],[0, 2]]))