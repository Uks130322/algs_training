# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/


def findAnagrams(self, s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []
    word = dict()
    for letter in p:
        word[letter] = word.get(letter, 0) + 1
    begin = 0
    end = len(p) - 1
    result = []
    string_part = dict()
    for letter in s[begin:end + 1]:
        string_part[letter] = string_part.get(letter, 0) + 1
    while end < len(s):
        if word == string_part:
            result.append(begin)
        string_part[s[begin]] -= 1
        if string_part[s[begin]] == 0:
            string_part.pop(s[begin])
        begin += 1
        end += 1
        if end == len(s):
            break
        else:
            string_part[s[end]] = string_part.get(s[end], 0) + 1
    return result

print(findAnagrams(0, s = "cbaebabacd", p = "abc"))
print(findAnagrams(0, s = "abab", p = "ab"))
print(findAnagrams(0, s = "abab", p = "abc"))