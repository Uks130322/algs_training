# https://leetcode.com/problems/3sum/description/


def threeSum(self, nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()
    nums_i_dict = dict()
    for i in range(len(nums) - 1):
        if nums[i] in nums_i_dict:
            continue
        else:
            nums_i_dict[nums[i]] = i
        nums_dict = dict()
        summa = 0 - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] in nums_dict:
                if nums[j] == nums_dict[nums[j]]:
                    triple = sorted([nums[i], nums[j], nums_dict[nums[j]]])
                    if not result or result[-1] != triple:
                        result.append(triple)
                    else:
                        continue
                    # break
                else:
                    result.append(sorted([nums[i], nums[j], nums_dict[nums[j]]]))
                nums_dict.pop(nums[j])
                # break
            else:
                nums_dict[summa - nums[j]] = nums[j]
    return result

print(threeSum(0, [-1,0,1,2,-1,-4, -3]))
print(threeSum(0, [0,1,-1, -1, 1, 0]))
print(threeSum(0, [0,0,0, 0]))
print(threeSum(0, [3,0,-2,-1,1,2,-4, 4, 5]))
print(threeSum(0, [0,2,2,3,0,1,2,3,-1,-4,2]))
print(threeSum(0, [-4,2,2,2,2,2,2,2,2]))