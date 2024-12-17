"""https://leetcode.com/problems/container-with-most-water/"""


def maxArea(height: list[int]) -> int:
    maximum = 0
    begin = 0
    end = len(height) - 1
    while begin < end:
        volume = min(height[begin], height[end]) * (end - begin)
        maximum = max(maximum, volume)
        if height[begin] >= height[end]:
            end -= 1
        else:
            begin += 1

    return maximum

print(maxArea([1,1]))