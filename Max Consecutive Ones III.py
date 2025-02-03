# https://leetcode.com/problems/max-consecutive-ones-iii/description/
from collections import OrderedDict


def longestOnes(self, nums: list[int], k: int) -> int:
    begin = 0
    end = 0
    reversed = 0
    longest = 0
    while end < len(nums):
        if nums[end] == 0:
            if reversed < k:
                reversed += 1
                end += 1
                longest = max(longest, end - begin)
            else:
                if nums[begin] == 0:
                    reversed -= 1
                begin += 1
        else:
            end += 1
            prefix = nums[end] if end < len(nums) else 0
            longest = max(longest, end - begin + prefix)

    return longest

lst1 = [0, 0, 1, 1, 0, 0, 1, 0, 1]
print(longestOnes(0, lst1, 1))
print(longestOnes(0, lst1, 2))
print(longestOnes(0, lst1, 4))
