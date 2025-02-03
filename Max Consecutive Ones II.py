# https://leetcode.com/problems/max-consecutive-ones-ii/description/


def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    left = 0
    right = 0
    longest = 0
    switched = False

    while right < len(nums):
        if nums[right] == 0:
            if not switched:
                switched = True
                longest = max(longest, right - left + 1)
                right += 1
            else:
                if nums[left] == 0:
                    left += 1
                    right = max(left, right)
                    switched = False
                else:
                    left += 1
                    right = max(left, right)
        else:
            longest = max(longest, right - left + 1)
            right += 1

    return longest


lst1 = [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1]

print(findMaxConsecutiveOnes(0, lst1))