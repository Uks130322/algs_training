# https://leetcode.com/problems/two-sum/description/


def twoSum(self, nums: list[int], target: int) -> list[int]:
    num_dict = dict()
    for i in range(len(nums)):
        if nums[i] in num_dict:
            return [num_dict[nums[i]], i]
        else:
            num_dict[target - nums[i]] = i

print(twoSum(0, nums=[2,7,11,15], target=18))