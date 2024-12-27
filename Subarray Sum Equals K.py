# https://leetcode.com/problems/subarray-sum-equals-k/description/


def subarraySum(self, nums: list[int], k: int) -> int:
    prev_sum = 0
    sums = {0: 1}
    result = 0
    for n in nums:
        prev_sum += n
        if prev_sum - k in sums.keys():
            result += sums[prev_sum - k]
        sums[prev_sum] = sums.get(prev_sum, 0) + 1
        print(sums, result)
    return result


print(subarraySum(1, [-1,-1,2,2], 0))
print(subarraySum(1, [1,1,1], 2))
print(subarraySum(1, [1,2,3], 3))
print(subarraySum(1, [1,2,1,2,1], 3))
print(subarraySum(1, [1], 2))




