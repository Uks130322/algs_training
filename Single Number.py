# https://leetcode.com/problems/single-number/description/


def singleNumber(self, nums: list[int]) -> int:
    # nums_dict = dict()
    # for num in nums:
    #     if num in nums_dict:
    #         nums_dict.pop(num)
    #     else:
    #         nums_dict[num] = True
    # return list(nums_dict.keys())[0]
    number = 0
    for num in nums:
        number ^= num
    return number


print(singleNumber(0, [2, 1, 2, 3, 3]))