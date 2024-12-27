# https://leetcode.com/problems/squares-of-a-sorted-array/description/


def sortedSquares(self, nums: list[int]) -> list[int]:
    if nums[0] >= 0:
        return [num ** 2 for num in nums]
    elif nums[-1] <= 0:
        return [nums[i] ** 2 for i in range(len(nums) - 1, -1, -1)]
    else:
        right = 0
        while nums[right] < 0:
            right += 1
        left = right - 1
        result = []
        while left >= 0 or right <= len(nums) - 1:
            print(left, right)
            if left >= 0 and (right > len(nums) - 1 or nums[left] ** 2 <= nums[right] ** 2):
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1
        return result

print(sortedSquares(1, [-3, -1, 1, 2, 5, 7]))
print(sortedSquares(1, [-3, -1]))
print(sortedSquares(1, [-1, 2, 2]))
print(sortedSquares(1, [1, 5]))
print(sortedSquares(1, [-4,-1,0,3,10]))