# https://leetcode.com/problems/sliding-window-median/description/


def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
    result = []
    if k == 1:
        return nums
    interval = sorted(nums[:k])
    result.append((interval[k // 2] + interval[k // 2 + (k % 2 - 1)]) / 2)
    i = k
    while i < len(nums):
        out = nums[i - k]
        add = nums[i]
        j = 0
        for j in range(k):
            # print(interval[j], out)
            if interval[j] == out:
                # print(interval)
                interval = interval[:j] + interval[j + 1:]
                break
        for j in range(k - 1):
            # print(interval, result)
            if interval[j] <= add:
                if j < k - 2:
                    if interval[j + 1] > add:
                        interval = interval[:j + 1] + [add] + interval[j + 1:]
                        break
                    else:
                        continue
                else:
                    interval.append(add)
                    break
            else:
                interval = interval[:j] + [add] + interval[j:]
                break

        result.append((interval[k // 2] + interval[k // 2 + (k % 2 - 1)]) / 2)
        i += 1

    return result


# print(medianSlidingWindow(0, nums = [1,3,-1,-3,5,3,6,7], k = 3))
# print(medianSlidingWindow(0, nums = [1,2,3,4,2,3,1,4,2], k = 3))
print(medianSlidingWindow(0, nums = [1,4,2,3], k = 4))
print(medianSlidingWindow(0, nums = [1,2], k = 1))