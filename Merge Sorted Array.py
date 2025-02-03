# https://leetcode.com/problems/merge-sorted-array/description/
# both functions works correctly, second is expected but first one works faster

def merge_0(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    result = []
    i1 = 0
    i2 = 0
    nums3 = nums1[:m + 1]
    while i1 < m or i2 < n:
        if i1 < m and i2 < n:
            if nums3[i1] <= nums2[i2]:
                result.append(nums3[i1])
                i1 += 1
            else:
                result.append(nums2[i2])
                i2 += 1
        elif i1 < m:
            result += nums3[i1:]
            break
        elif i2 < n:
            result += nums2[i2:]
            break
    nums1[:] = result[:n + m]
    return nums1


def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i1 = m - 1
    i2 = n - 1
    i3 = m + n - 1
    for end in range(i3, -1, -1):
        if i1 < 0:
            nums1[end] = nums2[i2]
            i2 -= 1
        elif i2 < 0:
            nums1[end] = nums1[i1]
            i1 -= 1
        elif nums1[i1] > nums2[i2]:
            nums1[end] = nums1[i1]
            i1 -= 1
        elif nums1[i1] <= nums2[i2]:
            nums1[end] = nums2[i2]
            i2 -= 1
    return nums1


print(merge(0, [1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge(0, [2,0], 1, [1], 1))


