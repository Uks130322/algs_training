"""https://leetcode.com/problems/partition-labels/description/"""


def partitionLabels(self, s: str) -> list[int]:
    letters = dict()
    result = []
    for i in range(len(s)):
        if s[i] not in letters:
            letters[s[i]] = [i, i]
        else:
            letters[s[i]][1] = i

    start = -1
    end = -1
    for index, item in enumerate(s):
        if start < 0:
            start = letters[item][0]
        if end < 0:
            end = letters[item][1]
            if start == end:
                result.append(1)
                start = -1
                end = -1
            continue
        end = max(end, letters[item][1])
        if index == end:
            result.append(end - start + 1)
            start = -1
            end = -1

    return result


print(partitionLabels(0, "eccbbbbdec"))  # [10]
print(partitionLabels(0, "caedbdeddag"))  # [1, 9, 1]
print(partitionLabels(0, "caedbdedda"))  # [1, 9]
print(partitionLabels(0, "ababcbacadefegdehijhklij"))  # [9,7,8]

