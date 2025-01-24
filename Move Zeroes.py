# https://leetcode.com/problems/move-zeroes/description/


def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1:
        return
    begin, end = 0, 1
    while end < len(nums):
        if nums[begin] != 0:
            begin += 1
            end += 1
        else:
            if nums[end] != 0:
                nums[begin] = nums[end]
                nums[end] = 0
                begin += 1
                end += 1
            else:
                end += 1