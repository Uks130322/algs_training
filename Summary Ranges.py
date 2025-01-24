# https://leetcode.com/problems/summary-ranges/description/


def summaryRanges(self, nums: list[int]) -> list[str]:
    result = []
    begin = nums[0]
    end = nums[0]
    for num in nums[1:]:
        if num == end + 1:
            if isinstance(begin, int):
                begin = str(begin) + '->'
            end = num
        else:
            if begin == end:
                result.append(str(begin))
            else:
                result.append(begin + str(end))
            begin, end = num, num
    if begin == end:
        result.append(str(begin))
    else:
        result.append(begin + str(end))

    return result

print(summaryRanges(0, [0, 1, 2, 4, 5, 7]))
print(summaryRanges(0, [0, 1]))