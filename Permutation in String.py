# https://leetcode.com/problems/permutation-in-string/


def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    word = dict()
    for letter in s1:
        word[letter] = word.get(letter, 0) + 1

    split = dict()
    index = 0
    while index < len(s2) + 1:
        if index < len(s1):
            split[s2[index]] = split.get(s2[index], 0) + 1
            index += 1
        else:
            if split == word:
                return True
            if index == len(s2):
                return False
            split[s2[index]] = split.get(s2[index], 0) + 1
            split[s2[index - len(s1)]] -=1
            if split[s2[index - len(s1)]] == 0:
                split.pop(s2[index - len(s1)])
            index += 1
        print(split)
    else:
        return False

print(checkInclusion(0, s1 = "ab", s2 = "eidbjaooo"))
print(checkInclusion(0, s1 = "adc", s2 = "dcda"))