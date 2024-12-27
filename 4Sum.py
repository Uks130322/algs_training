# https://leetcode.com/problems/4sum/description/


def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    two_sums = dict()
    for i in range(len(nums) - 1):
        previous = []
        for j in range(i + 1, len(nums)):
            if not previous or nums[j] != previous:
                two_sums[target - nums[i] - nums[j]] = two_sums.get(target - nums[i] - nums[j], []) + [[i, j]]
                previous = nums[j]
    # print(two_sums)
    result = set()
    seen = set()
    for sums in two_sums:
        if target - sums not in two_sums:
            continue
        if sums in seen or target - sums in seen:
            continue
        else:
            first = two_sums[sums]
            second = two_sums[target - sums]
            # print(first, second)
            for i in range(len(first)):
                for j in range(len(second)):
                    combo = first[i] + second[j]
                    # print(combo)
                    if len(set(combo)) != 4:
                        continue
                    result.add(tuple(sorted([nums[first[i][0]], nums[first[i][1]],
                            nums[second[j][0]], nums[second[j][1]]])))
                    # print(result)
            seen.add(sums)
            seen.add(target - sums)
    return [list(four) for four in result]


# print(fourSum(0,[1,0,-1,0,-2,2], target=0))
# print(fourSum(0,[2,2,2,2,2], target=8))
print(fourSum(0,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                 2,2], target=8))
