# https://leetcode.com/problems/valid-anagram/description/


def isAnagram(self, s: str, t: str) -> bool:
    s_dict = dict()
    for letter in s:
        s_dict[letter] = s_dict.get(letter, 0) + 1
    for letter in t:
        if letter not in s_dict:
            return False
        else:
            s_dict[letter] -= 1
            if s_dict[letter] == 0:
                s_dict.pop(letter)
    if s_dict == dict():
        return True
    else:
        return False


print(isAnagram(0, s = "anagram", t = "nagaram"))
print(isAnagram(0, "rat", t = "car"))